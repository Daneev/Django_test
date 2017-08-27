from django import forms
from .models import Order, Comment

from Apteki.models import Lekarstv

class OrderForm(forms.ModelForm):
    #lekarstvo = forms.ModelChoiceField(queryset=Lekarstv.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ["name"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]