from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('contacts/', ContactsView.as_view(), name="contacts"),
	path('info/', InfoView.as_view(), name="info"),
	path('services/', ServicesView.as_view(), name="services"),
	path('form/appointment/checkout', AppointmentCheckout.as_view(), name="appointment_checkout"),
]
