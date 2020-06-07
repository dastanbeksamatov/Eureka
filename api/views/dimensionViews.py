from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wordDictionary.models import Dimension
from ..serializers import DimensionSerializer


class DimensionList(APIView):
    def get(self, request, format=None):
        queryset = Dimension.objects.all()
        serializer = DimensionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(seld, request, format=None):
        serializer = DimensionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class DimensionDetail(APIView):
    def get_dimension(self, name):
        try:
            return Dimension.objects.filter(name=name)
        except Dimension.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        dimension = self.get_dimension(slug)
        serializer = DimensionSerializer(dimension[0])
        return Response(serializer.data)
