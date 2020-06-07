from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from wordDictionary.models import Lemma, Word
from ..serializers import (LemmaListSerializer, LemmaDetailSerializer,
                           RelatedWordSerializer)
from ..utils import getDimOptions, getFeatures
from ..pagination import PaginationMixin


class LemmaList(APIView, PaginationMixin):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, format=None):
        lemmas = Lemma.objects.all()
        page = self.paginate_queryset(lemmas)
        if page is not None:
            serializer = LemmaDetailSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = LemmaListSerializer(lemmas, many=True)
        return Response(serializer.data,
                        headers={"Access-Control-Allow-Origin": "*"})

    def options(self, request):
        return Response(status=status.HTTP_200_OK,
                        headers={"Access-Control-Allow-Origin": "*",
                                 "Access-Control-Allow-Headers":
                                 "access-control-allow-origin"})

    def post(self, request, format=None):
        serializer = LemmaListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LemmaDetail(APIView):
    def get_lemma(self, name):
        try:
            return Lemma.objects.get(name=name)
        except Lemma.DoesNotExist:
            return Http404

    def get_related_words(self, pk):
        try:
            related_words = Word.objects.filter(lemma=pk)
            return related_words
        except Word.DoesNotExist:
            return Http404

    def get(self, request, slug):
        lemma = self.get_lemma(name=slug)
        serializer = LemmaDetailSerializer(lemma)
        related_words = self.get_related_words(lemma.id)
        words = RelatedWordSerializer(related_words, many=True)
        lemma_data = serializer.data
        words_data = words.data
        for i in words_data:
            dims = getDimOptions(i['tagset'])
            i['tagset'] = getFeatures(i['tagset'])
            i['dimensions'] = dims
        lemma_data['related_words'] = words_data
        return Response(lemma_data,
                        headers={"Access-Control-Allow-Origin": "*"})

    def options(self, request, slug):
        return Response(status=status.HTTP_200_OK,
                        headers={"Access-Control-Allow-Origin": "*",
                                 "Access-Control-Allow-Headers":
                                 "access-control-allow-origin"})
