from rest_framework import viewsets
from rest_framework import permissions

from .models import RussianWord, EnglishWord
from .serializer import RussianWordSerializer, EnglishWordSerializer


class RussianWordViewSet(viewsets.ModelViewSet):
    queryset = RussianWord.objects.all().order_by('id')
    serializer_class = RussianWordSerializer
    permission_classes = [permissions.AllowAny]


class EnglishWordViewSet(viewsets.ModelViewSet):
    queryset = EnglishWord.objects.all().order_by('id')
    serializer_class = EnglishWordSerializer
    permission_classes = [permissions.AllowAny]
