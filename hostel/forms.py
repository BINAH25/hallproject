from django import forms
from hostel . models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
