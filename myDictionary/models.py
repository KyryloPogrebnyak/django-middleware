from django.db import models
from django.forms import ModelForm
# Create your models here.

class Word(models.Model):
    english = models.CharField(max_length=40)
    german = models.CharField(max_length=40)

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'