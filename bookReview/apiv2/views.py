from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

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


#-------------------------------FOR V3-----------------

class BookViewSet(viewsets.ModelViewSet):
	queryset = models.Book.objects.all()
	serializer_class = serializers.BookSerializer

	@detail_route(methods=['get'])
	def reviews(self, request, pk=None):
		book = self.get_object()
		serializer = serializers.ReviewSerializer(
				book.reviews.all(), many=True)
		return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer

