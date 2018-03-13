from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Event, Guide, Review

# Create your views here.

# main page
def affiche(request):
    return render(request, 'events/affiche.html')


# guides
def guides(request):
    guides = Guide.objects.all()
    head = {
    "title": "Guides"
    }
    context = {"guides": guides, 'head': head}
    return render(request, 'events/guides.html', context)

def show_guide(request, nick):
    guide = Guide.objects.get(nick=nick)
    head = {'title': guide.name}
    context = {"guide": guide, 'head': head}
    return render(request, 'events/show_guide.html', context)


# feedback
def reviews(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, 'events/reviews.html', context)


# Our projects
def projects(request):
    events = Event.objects.all()
    head = {
    "title": "Our Projects"
    }
    context = {'events': events, "head": head}
    return render(request, 'events/projects.html', context)

def show_project(request, permalink):
    event = Event.objects.get(permalink=permalink)
    context = {"event":event}
    return render(request, 'events/show_project.html', context)
