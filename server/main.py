from flask import Flask
from dotenv import load_dotenv
import wikipediaapi
import random
import os
import re

load_dotenv()
app = Flask(__name__)

# env
USER_AGENT = os.getenv("USER_AGENT")
PORT = os.getenv("PORT")

# wiki 
wiki = wikipediaapi.Wikipedia(user_agent=USER_AGENT, language='en')

# https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/People
people_page = wiki.page("Wikipedia:Vital_articles/Level/4/People")
links = people_page.links
keys = [key for key in links.keys() if "Wikipedia:" not in links[key].title]
random_person = None
title = None

def choose_article():
    global random_person, title
    random_person = wiki.page(keys[random.randint(0, len(keys))])
    title = random_person.title
    print("PAGE TITLE:")
    print(title)
    print()
    get_section_titles()

def redact_info(input: str) -> str:
    """ Attempts to remove revealing information from input string """
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

def get_section_titles():
    if random_person == None:
        choose_article()
    else:
        for section in random_person.sections:
            if len(section.text) > 0:
                print("TITLE:")
                print(redact_info(section.title))
                print()
                print("FULL TEXT:")
                print(redact_info(section.text))
                print()

def debug_env():
    print(f"usr_agent: {USER_AGENT}");
    print(f"port: {PORT}");

if __name__ == "__main__":
    # debug_env()
    # app.run(debug=True, port=PORT)
    choose_article()