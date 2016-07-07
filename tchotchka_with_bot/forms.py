from django import forms
from .models import Bot

class MsgForm(forms.ModelForm):
	class Meta:
		model = Bot
		fields = ('rep',)