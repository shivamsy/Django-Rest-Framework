from rest_framework import serializers
from . import models

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'title',
			'description',
			'price',
			'author',
			'publication',
			'created_at',
			)
		model = models.Book



class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'book',
			'rating',
			'comment',
			'created_at'
			)
		model = models.Review