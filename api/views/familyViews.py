from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wordDictionary.models import Family
from ..serializers import FamilySerializer


class FamilyList(APIView):
    def get(self, request, format=None):
        families = Family.objects.all()
        serializer = FamilySerializer(families, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FamilyDetail(APIView):
    def get_family(self, name):
        try:
            return Family.objects.filter(name=name)[:1]
        except Family.DoesNotExist:
            return Http404

    def get(self, request, slug):
        family = self.get_family(slug)
        serializer = FamilySerializer(family[0])
        return Response(serializer.data)
