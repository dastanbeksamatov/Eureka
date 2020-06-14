

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import MultipleObjectsReturned
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from ..models import Word
from ..serializers import WordSerializer
from ..utils import getDimOptions


class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'lemma']

    def options(self, request):
        return Response(status=status.HTTP_200_OK,
                        headers={"Access-Control-Allow-Origin": "*",
                                 "Access-Control-Allow-Headers":
                                 "access-control-allow-origin"})


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'name'

    def retrieve(self, request, name):
        word = self.get_object()
        serializer = WordSerializer(word)
        options = getDimOptions(serializer.data['tagset'])
        serializer_data = serializer.data
        serializer_data['dimensions'] = options
        return Response(serializer_data,
                        headers={"Access-Control-Allow-Origin": "*"})

    def options(self, request, name):
        return Response(status=status.HTTP_200_OK,
                        headers={"Access-Control-Allow-Origin": "*",
                                 "Access-Control-Allow-Headers":
                                     "access-control-allow-origin"})
