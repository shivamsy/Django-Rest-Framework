from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api import models
from api import serializers

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
		self.pagination_class.page_size = 5
		reviews = models.Review.objects.filter(book_id=pk)

		page = self.paginate_queryset(reviews)

		if page is not None:
			serializer = serializers.ReviewSerializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = serializers.ReviewSerializer(
				book.reviews.all(), many=True)
		return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer

