from dataclasses import dataclass
from json import JSONEncoder


class TopLanguagesEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@dataclass
class TopLanguageModel:
    language: str
    repos: list
    number_of_repos: int
