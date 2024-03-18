from django import forms

from .models import Town

class PostForm(forms.ModelForm):

    class Meta():
        model = Town
        fields = ('id','name', 'id_country')