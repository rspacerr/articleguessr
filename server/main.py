from flask import Flask
from dotenv import load_dotenv
import wikipediaapi
import random
import os

load_dotenv()
app = Flask(__name__)

# env
USER_AGENT = os.getenv("USER_AGENT")
PORT = os.getenv("PORT")

# wiki 
wiki = wikipediaapi.Wikipedia(user_agent=USER_AGENT, language='en')

# https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/People
people_page = wiki.page("Wikipedia:Vital_articles/Level/4/People")

def choose_article(): 
    links = people_page.links
    keys = [key for key in links.keys() if "Wikipedia:" not in links[key].title]
    random_person = wiki.page(keys[random.randint(0, len(keys))])
    print(random_person.title)
    print(random_person.summary)

def debug_env():
    print(f"usr_agent: {USER_AGENT}");
    print(f"port: {PORT}");

if __name__ == "__main__":
    # debug_env()
    choose_article()
    app.run(debug=True, port=PORT, debug=True)