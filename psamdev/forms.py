from django import forms
from . models import Message
from django.forms import ModelForm

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "number", "message"]
        
    # widgets = {
    #     "name" : forms.TextInput(attrs = {"class":"form-control", "placeholder":"Name"}),
    #     "email" : forms.TextInput(attrs = {"class":"form-control", "placeholder":"Email"}),
    #     "number" : forms.TextInput(attrs = {"class":"form-control", "placeholder":"Number"}),
    #     "message" : forms.Textarea(attrs = {"class":"form-control", "placeholder":"Message"}),
    # }