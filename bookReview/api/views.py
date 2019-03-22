from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.
def landing(request):
	return HttpResponse('<h1>Hello</h1>')