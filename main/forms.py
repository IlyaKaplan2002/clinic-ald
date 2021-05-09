from django import forms

class AppointmentForm(forms.Form):
	name = forms.CharField(max_length = 100)
	age = forms.IntegerField(min_value=0)
	destination = forms.ChoiceField(choices=(('prm', 'Первичное'), ('sec', 'Вторичное')), widget=forms.RadioSelect)
	phone = forms.CharField(max_length="11")
	action = forms.ChoiceField(choices=(('1', 'first'), ('2', 'second')), widget=forms.Select)