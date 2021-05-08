from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('about/', AboutView.as_view(), name="about"),
	path('contacts/', ContactsView.as_view(), name="contacts"),
	path('single/', SingleView.as_view(), name="single"),
	path('gallery/', GalleryView.as_view(), name="galley"),
	path('typography/', TypographyView.as_view(), name="typography"),
]
