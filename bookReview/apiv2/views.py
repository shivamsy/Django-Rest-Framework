from django.shortcuts import get_object_or_404
from rest_framework import generics

from . import models
from . import serializers

class ListCreateBook(generics.ListCreateAPIView):
	queryset = models.Book.objects.all()
	serializer_class = serializers.BookSerializer

class RetrieveUpdateDestroyBook(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Book.objects.all()
	serializer_class = serializers.BookSerializer

class ListCreateReview(generics.ListCreateAPIView):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer

	def get_queryset(self):
		return self.queryset.filter(book_id=self.kwargs.get('book_pk'))

class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer

	def get_object(self):
		return get_object_or_404(
			self.get_queryset(),
			book_id=self.kwargs.get('book_pk'),
			pk=self.kwargs.get('pk')
			)

