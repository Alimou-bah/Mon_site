from turtle import width
from django import forms
from .models import Article

class Article_f(forms.ModelForm):
    date_pub=forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model =Article
        fields = ("title", "sumary", "content", "image", "date_pub",)