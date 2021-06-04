from django import forms
from .models import *

ACTIONS = (
	('1', 'first'),
	('2', 'second'),
)

DESTIONATIONS = (
	('prm', 'Первичное'),
	('sec', 'Вторичное')
)

class AppointmentForm(forms.Form):
	name = forms.CharField(max_length = 100)
	age = forms.IntegerField(min_value=0)
	destination = forms.ChoiceField(choices=DESTIONATIONS, widget=forms.RadioSelect)
	phone = forms.CharField(max_length="11")
	action = forms.ChoiceField(choices=ACTIONS, widget=forms.Select)

# class AppointmentForm(forms.ModelForm):
# 	class Meta:
# 		model = Entry
# 		fields = '__all__'
# 		widgets = {
# 			'destination' : forms.RadioSelect(),
# 			'action' : forms.Select(),
# 		}