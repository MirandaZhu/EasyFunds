from django.conf.urls import url

from . import views as events
from pages import views as pages
from events.models import Event
from pprint import pprint

try:
    events_list=Event.objects.values_list('permalink',flat=True)
    events_list=list(events_list)
    events_list='|'.join(events_list)
except:
    events_list='test'

# 主要项目应用程序


urlpatterns = [
        url(r'^$', events.affiche, name='affiche'),
        # project
        url(r'projects/$', events.projects, name='projects'),
        # project labor
        url(r'^(?P<permalink>' + events_list + ')/', events.show_project, name='show_project'),
        # guide
        url(r'team/$', events.guides, name='guides'),
        # guide introduction
        url(r'team/(?P<nick>\w+)/$', events.show_guide, name='show_guide'),
        # feedback
        url(r'feedback/$', events.reviews, name='index'),
        # contacts
        url(r'contacts/$', pages.page, {"page": "contacts"}),
        ]
