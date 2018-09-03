from django.conf.urls import url

from . import views

app_name = 'loty'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poczatek>\d{4}-\d{2}-\d{2})_(?P<koniec>\d{4}-\d{2}-\d{2})/$', views.lista_lotow, name='index'),
	# ex: /polls/5/
	#url(r'^(?P<pk>[0-9]+)/$', views.SzczegolyView.as_view(), name='szczegoly'),
    url(r'^(?P<lot_id>[0-9]+)/$', views.szczegoly, name='szczegoly'),
    # ex: /polls/5/results/
	#url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
