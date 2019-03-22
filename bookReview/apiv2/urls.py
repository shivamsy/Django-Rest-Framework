from django.urls import path, include

from . import views

app_name='apiv2'

urlpatterns = [
	path('', views.ListCreateBook.as_view(), name='ListCreateBook'),
	path('<int:pk>', 
			views.RetrieveUpdateDestroyBook.as_view(),
			name='DetailBook'),
	path('<int:book_pk>/reviews/',
			views.ListCreateReview.as_view(),
			name='ListReview'),
	path('<int:book_pk>/reviews/<int:pk>/',
			views.RetrieveUpdateDestroyReview.as_view(),
			name='DetailReview'),

	]