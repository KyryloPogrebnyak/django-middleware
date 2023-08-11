from django.db import models
from django.forms import ModelForm
# Create your models here.

class Word(models.Model):
    english = models.CharField(max_length=30)
    german = models.CharField(max_length=30)

    def __str__(self):
        return self.english

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'