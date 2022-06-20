from django.http import HttpResponse


def index(request):
	return HttpResponse('Hello, world. You are at that polls index.')


def hello(request):
	return HttpResponse('got some json?')
