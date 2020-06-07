

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from wordDictionary.models import Word
from ..serializers import WordListSerializer, WordDetailSerializer
from ..utils import getDimOptions
from ..pagination import PaginationMixin


class WordList(APIView, PaginationMixin):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, format=None, *args, **kwargs):
        words = Word.objects.all()
        page = self.paginate_queryset(words)
        if page is not None:
            serializer = WordDetailSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = WordListSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WordListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordDetail(APIView):
    def get_word(self, name):
        try:
            return Word.objects.filter(name=name)[:1]
        except Word.DoesNotExist:
            return Http404

    def get(self, request, slug):
        word = self.get_word(slug)
        serializer = WordDetailSerializer(word[0])
        options = getDimOptions(serializer.data['tagset'])
        serializer_data = serializer.data
        serializer_data['dimensions'] = options
        return Response(serializer_data,
                        headers={"Access-Control-Allow-Origin": "*"})

    def options(self, request, slug):
        return Response(status=status.HTTP_200_OK,
                        headers={"Access-Control-Allow-Origin": "*",
                                 "Access-Control-Allow-Headers":
                                     "access-control-allow-origin"})
