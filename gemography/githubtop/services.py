import requests
from datetime import date
import dateutil.relativedelta

from gemography.githubtop.errors import SchemaChangedError
from gemography.githubtop.models import TopLanguageModel
from gemography.settings import GITHUB_SEARCH_API


class ReposService:
    def top_languages(self):
        top_starred_dict = self.request_top_starred()
        return self._extract_top_languages(top_starred_dict)

    @staticmethod
    def request_top_starred():
        thirty_days_ago = date.today() + dateutil.relativedelta.relativedelta(days=-30)
        thirty_days_ago_str = thirty_days_ago.strftime('%Y-%m-%d')
        thirty_days_ago_query = f'created:>{thirty_days_ago_str}'
        params = {'q': thirty_days_ago_query, 'sort': 'stars', 'order': 'desc', 'per_page': 100}
        response = requests.get(GITHUB_SEARCH_API, params=params)
        return response.json() if response.ok else None

    @staticmethod
    def _extract_top_languages(top_starred):
        top_languages = {}
        try:
            # build result
            for item in top_starred['items']:
                language = item['language']
                if language not in top_languages:
                    top_languages[language] = TopLanguageModel(language, [], 0)
                top_languages[language].repos.append(item)
                top_languages[language].number_of_repos += 1

            # return result sorted by number of repos
            return sorted(list(top_languages.values()),
                          key=lambda k: getattr(k, 'number_of_repos'),
                          reverse=True)
        except KeyError:
            raise SchemaChangedError()
