from django import forms
from .models import *

ACTIONS = (
	('1', 'Приём врача-кардиолога(с регистрацией и расшифровкой ЭКГ)'),
	('2', 'Консультация врача-кардиолога на дому у пациента (с регистрацией и расшифровкой ЭКГ)'),
	('3', 'Регистрация и расшифровка ЭКГ'),
	('4', 'Регистрация и расшифровка ЭКГ с ритмограммой'),
	('5', 'Суточное (холтеровское) мониторирование ЭКГ'),
	('6', 'Суточное мониторирование артериального давления'),
)

DESTIONATIONS = (
	('prm', 'Первичный'),
	('sec', 'Повторный')
)

class AppointmentForm(forms.Form):
	name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
	age = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
	destination = forms.ChoiceField(choices=DESTIONATIONS, widget=forms.RadioSelect(attrs={'class' : 'myfieldclass'}))
	phone = forms.CharField(max_length="11", widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
	action = forms.ChoiceField(choices=ACTIONS, widget=forms.Select(attrs={'class': 'myfieldclass'}))

# class AppointmentForm(forms.ModelForm):
# 	class Meta:
# 		model = Entry
# 		fields = '__all__'
# 		widgets = {
# 			'destination' : forms.RadioSelect(),
# 			'action' : forms.Select(),
# 		}
