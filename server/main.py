from flask import Flask, jsonify, session
from dotenv import load_dotenv
from article import Article
import wikipediaapi
import random
import os
import re
import secrets

load_dotenv()
app = Flask(__name__)
app.config.update(
   SESSION_PERMANENT=False, 
   SESSION_TYPE="filesystem",
   SESSION_USE_SIGNER=True
)

# sessions key
app.secret_key = secrets.token_hex(16)

# env
USER_AGENT = os.getenv("USER_AGENT")
PORT = os.getenv("PORT")

# wiki 
wiki = wikipediaapi.Wikipedia(user_agent=USER_AGENT, language='en')

# https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/People
people_page = wiki.page("Wikipedia:Vital_articles/Level/4/People")
links = people_page.links
keys = [key for key in links.keys() if "Wikipedia:" not in links[key].title]
article_sessions = {} 
tokens = {}
sections = []

def redact_info(input: str) -> str:
    """ Attempts to remove revealing information from input string """
    if 'token' not in session:
        # TODO: invalid session
        pass

    title = session['token'].get_title()
    tokens = title.split(" ");
    last_token = tokens[len(tokens)-1]
    censored = input.replace(title, "⬛"*len(title))

    if len(tokens) > 1:
        censored = censored.replace(tokens[0], "⬛"*len(tokens[0]))

    """ 
    If last token is not a roman numeral, or the middle word is not "of" or "the", assume it is a name and redact it
    Conditions are not mutually exclusive, but should in theory have a high success rate (failure is XXXX the/of <adjective/place> [Roman Numeral])
    """
    has_roman = re.search("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", last_token)
    adjective_name = len(tokens) == 3 and (tokens[1] == "of" or tokens[1] == "the")
    if not has_roman and not adjective_name:
        censored = censored.replace(last_token, "⬛"*len(last_token))
    return censored

@app.route("/")
async def session_init():
    if 'token' not in session:
        session['token'] = secrets.token_urlsafe(32)
        print("token not in session")
    if session['token'] not in article_sessions:
        await choose_article()
    return f"Your token is {session['token']}, and the article is {article_sessions[session['token']].title}", 201

async def choose_article():
    person = wiki.page(keys[random.randint(0, len(keys))])
    sections = [sec for sec in person.sections if len(sec.text) > 0 and sec.title != "Further reading" and sec.title != "See also" and sec.title != "External links"]
    article_sessions[session['token']] = Article(person, person.title, sections)
    return "", 201

@app.route("/api/section")
def get_section():
    if 'token' not in session:
        # TODO: invalid session, force reload page
        pass

    rand = random.randint(0, len(sections))
    section = sections[rand]
    print(jsonify({
        "title": redact_info(section.title),
        "text": redact_info(section.text)
    }))
    return jsonify({
        "title": redact_info(section.title),
        "text": redact_info(section.text)
    }), 201

def debug_env():
    print(f"usr_agent: {USER_AGENT}")
    print(f"port: {PORT}")

if __name__ == "__main__":
    app.run(debug=True, port=PORT)