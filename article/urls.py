from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    # ex: /
    url(r'^$', views.home, name='home'),
    # ex:/1
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]