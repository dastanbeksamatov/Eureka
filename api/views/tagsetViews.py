from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wordDictionary.models import TagSet
from ..serializers import TagSetSerializer


class TagSetList(APIView):
    def get(self, request, format=None):
        tagsets = TagSet.objects.all()
        serializer = TagSetSerializer(tagsets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagSetDetail(APIView):
    def get_tagset(self, pk):
        try:
            return TagSet.objects.get(pk=pk)
        except TagSet.DoesNotExist:
            return Http404

    def get(self, request, pk):
        tagset = self.get_tagset(pk)
        serializer = TagSetSerializer(tagset)
        return Response(serializer.data)
