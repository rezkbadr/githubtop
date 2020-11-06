from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from gemography.githubtop.models import TopLanguageModel
from gemography.githubtop.services import ReposService


class TestServices(TestCase):
    def setUp(self):
        self.repos_service = ReposService()

    @patch('gemography.githubtop.services.requests.get')
    def test_request_top_starred(self, mock_get):
        mock_get.return_value.ok = True
        repos = self.repos_service.request_top_starred()
        self.assertIsNotNone(repos)

    def test_extract_top_languages(self):
        top_starred = {'items': [
            {'language': 'Python'},
            {'language': 'Python'},
            {'language': 'Java'},
        ]}
        result = self.repos_service._extract_top_languages(top_starred)
        expected = [TopLanguageModel('Python', [{'language': 'Python'},
                                                {'language': 'Python'}], 2),
                    TopLanguageModel('Java', [{'language': 'Java'}], 1)]
        self.assertEqual(result, expected)


class TestAPI(APITestCase):
    def test_top_languages(self):
        url = reverse('top_languages')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
