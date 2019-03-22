from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers

# Create your views here.

class ListCreateBook(APIView):
	def get(self, request, format=None):
		books = models.Book.objects.all()
		serializer = serializers.BookSerializer(books, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.BookSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
