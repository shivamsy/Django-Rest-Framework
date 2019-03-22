from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=150, null=False, blank=False)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	author = models.CharField(max_length=100, null=False, blank=False)
	publication = models.CharField(max_length=100, null=False, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.title)

class Review(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
	rating = models.IntegerField()
	comment = models.TextField(blank=True, default='')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(book.title)+"\'s rating"