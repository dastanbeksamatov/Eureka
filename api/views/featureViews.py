from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wordDictionary.models import Feature
from ..serializers import FeatureListSerializer, FeatureDetailSerializer


class FeatureList(APIView):
    def get(self, request, format=None):
        features = Feature.objects.all()
        serializer = FeatureListSerializer(features, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeatureListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)


class FeatureDetail(APIView):
    def get_feature(self, name):
        try:
            return Feature.objects.filter(name=name)
        except Feature.DoesNotExist:
            return Http404

    def get(self, request, slug):
        feature = self.get_feature(slug)
        serializer = FeatureDetailSerializer(feature[0])
        return Response(serializer.data)
