from django.shortcuts import render
from django.views.generic import TemplateView

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

class SingleView(TemplateView):
	template_name = "single.html"

	def get(self, request):
		return render(request, self.template_name)

class GalleryView(TemplateView):
	template_name = "gallery.html"

	def get(self, request):
		return render(request, self.template_name)

class TypographyView(TemplateView):
	template_name = "typography.html"

	def get(self, request):
		return render(request, self.template_name)