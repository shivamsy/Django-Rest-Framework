from rest_framework import serializers
from api import models


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

class BookSerializer(serializers.ModelSerializer):
	reviews = serializers.HyperlinkedRelatedField(
							many=True, read_only=True
						)

	class Meta:
		fields = (
			'id',
			'title',
			'description',
			'price',
			'author',
			'publication',
			'reviews',
			'created_at',
			)
		model = models.Book


