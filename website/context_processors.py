from website.slogans import slogans
import random
from django.urls import reverse

def slogans_gen(request):
    slogan = random.choice(slogans)
    return {'slogan': slogan}

def main_menu(request):
    main_menu = [
    {
    "url":"/",
    "title":"EasyFunds",
    },
    {
    "url": reverse('projects'),
    "title": "Invest Projects",
    },
    {
    "url":reverse('guides'),
    "title":"FAQ",
    },
    #{
    #"url":"/contacts/",
    #"title":"Contact Us",
    #},
    {
    "url":"/feedback/",
    "title":"Contact Us",
    },
    ]
    return {'main_menu':main_menu}
