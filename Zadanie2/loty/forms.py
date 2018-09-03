# coding=utf-8

from django import forms
from loty.models import Pasazer, Samolot, Lot

class FilterForm(forms.Form):
    data = forms.DateTimeField(widget=forms.SelectDateWidget(empty_label=("Wybierz rok", "Wybierz miesiąc", "Wybierz dzień")))
#class StuffForm(forms.ModelForm):
#	class Meta:
#		model = Stuff
#		fields = ('name', 'count')
