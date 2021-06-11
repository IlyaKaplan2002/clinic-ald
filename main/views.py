from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import *
# import requests
from django.core.mail import send_mail
# import datetime
from django.conf import settings


class HomeView(TemplateView):
	template_name = "index.html"

	def get(self, request):
		context = {}
		context["pg_name"] = "home"
		return render(request, self.template_name, context)

class AboutView(TemplateView):
	template_name = "about.html"

	def get(self, request):
		context = {}
		context["pg_name"] = "about"
		return render(request, self.template_name,context)

class ContactsView(TemplateView):
	template_name = "contact.html"

	def get(self, request):
		context = {}
		context["pg_name"] = "contacts"
		return render(request, self.template_name, context)

class InfoView(TemplateView):
	template_name = "info.html"

	def get(self, request):
		context = {}
		context["pg_name"] = "info"
		return render(request, self.template_name, context)

class ServicesView(TemplateView):
	template_name = "services.html"

	def get(self, request):
		context = {}
		context["pg_name"] = "services"
		return render(request, self.template_name, context)

class AppointmentView(View):
	template_name = "appointment.html"
	ACTIONS = (
	    'Приём врача-кардиолога(с регистрацией и расшифровкой ЭКГ)',
	    'Консультация врача-кардиолога на дому у пациента (с регистрацией и расшифровкой ЭКГ)',
	    'Регистрация и расшифровка ЭКГ', 'Регистрация и расшифровка ЭКГ',
	    'Регистрация и расшифровка ЭКГ с ритмограммой',
	    'Суточное (холтеровское) мониторирование ЭКГ',
	    'Суточное мониторирование артериального давления',
	    'Суточное мониторирование артериального давления',
	)

	def get(self, request):
		context = {}
		context["pg_name"] = "appointment"
		form = AppointmentForm()
		context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		context["pg_name"] = "appointment"
		form = AppointmentForm(request.POST)
		if form.is_valid():
			context["data"] = form.cleaned_data["destination"]
			context["message"] = "Успешная запись на прием"
			subject = f"{form.cleaned_data['name']}"
			message_additional = '''
Форма: услуги\n
'''
			counter = 1
			for i in range(1, len(self.ACTIONS)):
				if form.cleaned_data[f"action{i}"]:
					message_additional += f"{counter}) {self.ACTIONS[i - 1]}\n"
					counter += 1
			message = f'''
Форма: Прием
Ответ: {form.cleaned_data["destination"]}

Форма: Услуга
Ответ: {form.cleaned_data["action"]}

Форма: ФИО
Ответ: {form.cleaned_data["name"]}

Форма: Возраст
Ответ: {form.cleaned_data["age"]}

Форма: Телефон
Ответ: {form.cleaned_data["phone"]}
'''
			message += message_additional
			send_from = settings.EMAIL_HOST_USER
			# to = ["kaplan.cardio@gmail.com"]
			to = ["mikaelan.itsmart@gmail.com"]
			send_mail(subject, message, send_from, to)
			return render(request, self.template_name, context)
		context["data"] = "error"
		return render(request, self.template_name, context)
	#
	# def send_message(self):
	# 	token = "ТУТ_ВАШ_ТОКЕН_КОТОРЫЙ_ВЫДАЛ_BotFather"
	# 	url = "https://api.telegram.org/bot"
	# 	channel_id = "@ИМЯ_КАНАЛА"
	# 	url += token
	# 	method = url + "/sendMessage"
	#
	# 	r = requests.post(method, data={
	# 		"chat_id": channel_id,
	# 		"text": text,
	# 	})
