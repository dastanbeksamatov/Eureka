from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wordDictionary.models import Language
from ..serializers import LanguageSerializer


class LanguageList(APIView):
    def get(self, request, format=None):
        queryset = Language.objects.all()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LanguageDetail(APIView):
    def get_language(self, name):
        try:
            return Language.objects.filter(name=name)
        except Language.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        language = self.get_language(slug)
        serializer = LanguageSerializer(language[0])
        return Response(serializer.data)
