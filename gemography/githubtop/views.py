from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from gemography.githubtop.services import ReposService


class TopLanguages(APIView):

    def get(self, request):
        top = ReposService().top_languages()
        return Response(top, status=status.HTTP_200_OK)
