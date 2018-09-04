from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from loty.models import Pasazer, Samolot, Lot
from django.template import loader
from django.db import transaction

def lista_lotow(request, poczatek, koniec):
    loty = Lot.objects.filter(czas_startu__range=[poczatek, koniec])

    return render(request, 'loty/index.html',
    {'lista_lotow':loty})

class IndexView(generic.ListView):
    template_name = 'loty/index.html'
    context_object_name = 'lista_lotow'

    def get_queryset(self):
        return Lot.objects.all()

def zakup_biletu(request, lot):
    imie = request.POST.get('imie', '')
    nazwisko = request.POST.get('nazwisko', '')

    with transaction.atomic():
        if lot.samolot.liczba_miejsc > lot.pasazerowie.all().count():
            pasazer = Pasazer(imie = imie, nazwisko = nazwisko)
            pasazer.save()
            lot.pasazerowie.add(pasazer)

def szczegoly(request, lot_id):
    lot = get_object_or_404(Lot, pk=lot_id)
    samolot = get_object_or_404(Samolot, pk=lot.samolot.id)

    if request.method == "POST":
        zakup_biletu(request, lot)
        something_irrelevant = -1

    return HttpResponse(render(request, 'loty/szczegoly.html', locals()))
