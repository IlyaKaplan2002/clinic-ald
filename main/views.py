from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import *

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
			return render(request, self.template_name, context)
		context["data"] = "error"
		return render(request, self.template_name, context)
