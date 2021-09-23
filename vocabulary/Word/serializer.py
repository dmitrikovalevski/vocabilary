from rest_framework import serializers
from rest_framework import permissions

from .models import RussianWord, EnglishWord


class RussianWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RussianWord
        fields = ['pk', 'russian', 'english']


class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWord
        fields = ['pk', 'english', 'russian']
