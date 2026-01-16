from wikipediaapi import WikipediaPage, WikipediaPageSection
import json
import typing
import re

STARTING_LIVES:int = 6

class GameInfo:
    def __init__(self, page: WikipediaPage, sections: typing.List[WikipediaPageSection]):
        self.active = True
        self.lives = min(STARTING_LIVES, len(sections)) 
        self.title = page.title
        self.url = page.canonicalurl
        self.sections = sections
        self.redacted = [self.redact(section.text) for section in sections]
        # self.guesses = set()
        
    def redact(self, section: WikipediaPageSection) -> str:
        tokens = self.title.split(" ");
        last_token = tokens[len(tokens)-1]
        censored = section.replace(self.title, "_"*len(self.title))

        if len(tokens) > 1:
            censored = censored.replace(tokens[0], "_"*len(tokens[0]))

        """ 
        If last token is not a roman numeral, or the middle word is not "of" or "the", assume it is a name and redact it
        Conditions are not mutually exclusive, but should in theory have a high success rate (failure is XXXX the/of <adjective/place> [Roman Numeral])
        """
        has_roman = re.search("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", last_token)
        adjective_name = len(tokens) == 3 and (tokens[1] == "of" or tokens[1] == "the")
        if not has_roman and not adjective_name:
            # censored = censored.replace(last_token, "⬛"*len(last_token))
            censored = censored.replace(last_token, "_"*len(last_token))
        return censored 
    
    def pop_section(self, token) -> typing.Tuple[str, bool]:
        if token != self.token or not self.active or self.lives <= 0:
            return ("Bad Request", False)
        
    def get_sections_raw(self) -> typing.List[WikipediaPageSection]:
        return self.page.sections

    def serialize(self):
        return {
            "url": self.url,
            "title": self.title,
            "sections": self.redacted,
            "lives": self.lives
        }

    """
    def get_sections_redacted(self) -> typing.List[str]:
        return self.game_sections.values()
    """

    def get_lives(self) -> int:
        return self.lives