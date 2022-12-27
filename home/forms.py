from django.forms import ModelForm
from django import forms
from home.models import Saya

class FormSaya(ModelForm):
    class Meta :
        model = Saya
        fields = '__all__'