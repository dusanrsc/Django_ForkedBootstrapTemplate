from django.shortcuts import render

# Create your views here.
# index/home page view
def index(requests):
	return render(requests, "index.html", {})

# about page view
def about(requests):
	return render(requests, "about.html", {})

# book page view
def book(requests):
	return render(requests, "book.html", {})

# menu page view
def menu(requests):
	return render(requests, "menu.html", {})