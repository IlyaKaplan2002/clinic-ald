from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import *
from django.core.mail import send_mail
from django.conf import settings


class HomeView(TemplateView):
	template_name = "index.html"

	def get(self, request):
		context = {}
		return render(request, self.template_name, context)

class ContactsView(TemplateView):
	template_name = "contacts.html"

	def get(self, request):
		context = {}
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

class AppointmentCheckout(View):
	ACTIONS = (
	    'Приём врача-кардиолога(с регистрацией и расшифровкой ЭКГ)',
	    'Консультация врача-кардиолога на дому у пациента (с регистрацией и расшифровкой ЭКГ)',
	    'Регистрация и расшифровка ЭКГ',
	    'Регистрация и расшифровка ЭКГ с ритмограммой',
	    'Суточное (холтеровское) мониторирование ЭКГ',
	    'Суточное мониторирование артериального давления',
	)
	def post(self, request):
		print(request.POST)
		form = AppointmentForm(request.POST)
		subject = f"{form.data['name']}"
		message_additional = '''
Форма: услуги\n
'''
		counter = 1
		for i in range(1, len(self.ACTIONS) + 1):
			if form.data.get(f"action{i}", False):
				message_additional += f"{counter}) {self.ACTIONS[i - 1]}\n"
				counter += 1
		message = f'''
Форма: Прием
Ответ: {form.data.get("destination", "Не указан")}

Форма: ФИО
Ответ: {form.data["name"]}

Форма: Возраст
Ответ: {form.data["age"]}

Форма: Телефон
Ответ: {form.data["phone"]}
'''
		message += message_additional
		send_from = settings.EMAIL_HOST_USER
		to = ["kaplan.cardio@gmail.com"]
		# to = ["mikaelan.itsmart@gmail.com"]
		send_mail(subject, message, send_from, to)
		return redirect("main:home")


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
