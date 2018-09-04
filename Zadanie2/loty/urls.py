from django.conf.urls import url

from . import views

app_name = 'loty'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poczatek>\d{4}-\d{2}-\d{2})_(?P<koniec>\d{4}-\d{2}-\d{2})/$', views.lista_lotow, name='index'),
    url(r'^(?P<lot_id>[0-9]+)/$', views.szczegoly, name='szczegoly'),
]
