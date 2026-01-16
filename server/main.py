from flask import Flask, jsonify, session
from flask_session import Session
from flask_cors import CORS
from dotenv import load_dotenv
from game_info import GameInfo
import typing
import wikipediaapi
import random
import os
import secrets

load_dotenv()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.update(
   SESSION_PERMANENT=False, 
   SESSION_TYPE="filesystem",
   SESSION_USE_SIGNER=True
)
Session(app)
# sessions key
app.secret_key = secrets.token_hex(16)

# env
USER_AGENT = os.getenv("USER_AGENT")
PORT = os.getenv("PORT")

# wiki 
# https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/People
wiki = wikipediaapi.Wikipedia(user_agent=USER_AGENT, language='en')
people_page = wiki.page("Wikipedia:Vital_articles/Level/4/People")
links = people_page.links
keys = [key for key in links.keys() if "Wikipedia:" not in links[key].title]

# token -> GameInfo 
session_data: typing.Dict[str, GameInfo] = {}

@app.route("/api/session")
def session_init():
    #new_sesh = False
    if 'token' not in session:
        session['token'] = secrets.token_urlsafe(32)
    #    new_sesh = True
    token = session['token']
    if token not in session_data:
        session_data[session['token']] = reset_session()
    return jsonify(session_data[session['token']].serialize())

def choose_article():
    return wiki.page(keys[random.randint(0, len(keys))])

def reset_session() -> GameInfo:
    person = choose_article()
    sections = [sec for sec in person.sections if len(sec.text) > 0 and sec.title != "Further reading" and sec.title != "See also" and sec.title != "External links"]
    return GameInfo(person, sections)

@app.route("/api/section")
def get_section():
    if 'token' not in session:
        return f"Invalid session", 500
    
    # debug
    token = session['token']
    print("length: ", len(session_data[token].get_sections_redacted()))

    """
    TODO: Need to prevent grabbing the same section again
    """
    token = session['token']
    sections = session_data[token].get_sections_redacted()
    rand = random.randint(0, len(sections))
    section = sections[rand]
    
    # TODO: sections should be stored as a list, with each person's session token mapping to an individual list!
    
    print(jsonify({
        "title": section.title,
        "text": section.text
    }))
    return jsonify({
        "title": section.title,
        "text": section.text
    }), 201

def debug_env():
    print(f"usr_agent: {USER_AGENT}")
    print(f"port: {PORT}")

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
    # debug_env()