import requests
from datetime import date
import dateutil.relativedelta
from gemography.settings import GITHUB_SEARCH_API


class ReposService:
    def request_top_starred(self):
        thirty_days_ago = date.today() + dateutil.relativedelta.relativedelta(days=-30)
        thirty_days_ago_str = thirty_days_ago.strftime('%Y-%m-%d')
        thirty_days_ago_query = f'created:>{thirty_days_ago_str}'
        params = {'q': thirty_days_ago_query, 'sort': 'stars', 'order': 'desc', 'per_page': 100}
        response = requests.get(GITHUB_SEARCH_API, params=params)
        return response.json() if response.ok else None

    def top_languages(self):
        pass
