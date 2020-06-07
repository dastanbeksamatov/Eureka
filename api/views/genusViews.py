from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wordDictionary.models import Genus
from ..serializers import GenusSerializer


class GenusList(APIView):
    def get(self, request, format=None):
        genuses = Genus.objects.all()
        serializer = GenusSerializer(genuses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenusDetail(APIView):
    def get_genus(self, name):
        try:
            return Genus.objects.filter(name=name)[:1]
        except Genus.DoesNotExist:
            return Http404

    def get(self, request, slug):
        genus = self.get_genus(slug)
        serializer = GenusSerializer(genus[0])
        return Response(serializer.data)
