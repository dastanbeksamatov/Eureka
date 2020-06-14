from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Language
from ..serializers import LanguageSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']
