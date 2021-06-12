from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('about/', AboutView.as_view(), name="about"),
	path('contacts/', ContactsView.as_view(), name="contacts"),
	path('info/', InfoView.as_view(), name="info"),
	path('services/', ServicesView.as_view(), name="services"),
	path('appointment/', AppointmentView.as_view(), name="appointment"),
	path('redirect/<int:id>/', LinkCheckboxView.as_view(), name="linkcheckbox"),
]
