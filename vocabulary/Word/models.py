from django.db import models


class EnglishWord(models.Model):
    english = models.CharField(max_length=200)
    russian = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.english}'


class RussianWord(models.Model):
    english = models.CharField(max_length=200)
    russian = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.russian}'
