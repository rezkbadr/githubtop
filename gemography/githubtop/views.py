from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from gemography.githubtop.models import TopLanguagesEncoder
from gemography.githubtop.services import ReposService


class TopLanguages(APIView):
    repos_service = ReposService()

    def get(self, request):
        top = self.repos_service.top_languages()
        result = {'result': top}
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK, encoder=TopLanguagesEncoder)
