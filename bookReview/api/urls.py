from django.urls import path, include

from . import views

app_name='api'

urlpatterns = [
	path('', views.ListCreateBook.as_view(), name='ListCreateBook'),
	]