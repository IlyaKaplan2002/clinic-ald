from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import *
# import requests
from django.core.mail import send_mail
# import datetime


class HomeView(TemplateView):
	template_name = "index.html"

	def get(self, request):
		return render(request, self.template_name)

class AboutView(TemplateView):
	template_name = "about.html"

	def get(self, request):
		return render(request, self.template_name)

class ContactsView(TemplateView):
	template_name = "contact.html"

	def get(self, request):
		return render(request, self.template_name)

class InfoView(TemplateView):
	template_name = "info.html"

	def get(self, request):
		return render(request, self.template_name)

class ServicesView(TemplateView):
	template_name = "services.html"

	def get(self, request):
		return render(request, self.template_name)

class TypographyView(TemplateView):
	template_name = "typography.html"

	def get(self, request):
		return render(request, self.template_name)

class AppointmentView(View):
	template_name = "appointment.html"

	def get(self, request):
		context = {}
		form = AppointmentForm()
		context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		form = AppointmentForm(request.POST)
		if form.is_valid():
			context["data"] = form.cleaned_data["destination"]
			context["message"] = "Успешная запись на прием"
			subject = f"{form.cleaned_data['name']}"
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
			send_from = "kaplan.cardiology.bot@gmail.com"
			to = ["kaplan.cardio@gmail.com"]
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
