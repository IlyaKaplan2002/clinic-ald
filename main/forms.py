from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

ACTIONS = (
	('Приём врача-кардиолога(с регистрацией и расшифровкой ЭКГ', 'Приём врача-кардиолога(с регистрацией и расшифровкой ЭКГ'),
	('Консультация врача-кардиологана дому у пациента (с регистрацией и расшифровкой ЭКГ)', 'Консультация врача-кардиологана дому у пациента (с регистрацией и расшифровкой ЭКГ)'),
	('Регистрация и расшифровка ЭКГ', 'Регистрация и расшифровка ЭКГ'),
	('Регистрация и расшифровка ЭКГ с ритмограммой', 'Регистрация и расшифровка ЭКГ с ритмограммой'),
	('Суточное (холтеровское) мониторирование ЭКГ', 'Суточное (холтеровское) мониторирование ЭКГ'),
	('Суточное мониторирование артериального давления', 'Суточное мониторирование артериального давления'),
)

DESTIONATIONS = (
	('Первичный', 'Первичный'),
	('Повторный', 'Повторный')
)

class AppointmentForm(forms.Form):
	name = forms.CharField(label = _("name"), max_length = 100, widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
	age = forms.IntegerField(label = _("age"), min_value=0, widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
	destination = forms.ChoiceField(label = _("destination"), choices=DESTIONATIONS, widget=forms.RadioSelect(attrs={'class' : 'myfieldclass'}))
	phone = forms.CharField(label = _("phone"), max_length="11", widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
	# action = forms.ChoiceField(label = _("action"), choices=ACTIONS, widget=forms.Select(attrs={'class': 'myfieldclass'}))

	action1 = forms.BooleanField()
	action2 = forms.BooleanField()
	action3 = forms.BooleanField()
	action4 = forms.BooleanField()
	action5 = forms.BooleanField()
	action6 = forms.BooleanField()

# class AppointmentForm(forms.ModelForm):
# 	class Meta:
# 		model = Entry
# 		fields = '__all__'
# 		widgets = {
# 			'destination' : forms.RadioSelect(),
# 			'action' : forms.Select(),
# 		}
