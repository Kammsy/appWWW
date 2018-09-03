from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from loty.models import Pasazer, Samolot, Lot
from django.template import loader
from django.db import transaction
#from loty.forms import PasazerForm, SamolotForm, LotForm

def lista_lotow(request, poczatek, koniec):
    loty = Lot.objects.filter(czas_startu__range=[poczatek, koniec])

    return render(request, 'loty/index.html',
    {'lista_lotow':loty})

class IndexView(generic.ListView):
    template_name = 'loty/index.html'
    context_object_name = 'lista_lotow'

    def get_queryset(self):
        return Lot.objects.all()

    # def get_queryset(self):
    #     filter_val = self.request.GET.get('filter', 'give-default-value')
    #     order = self.request.GET.get('orderby', 'give-default-value')
    #     new_context = Update.objects.filter(
    #         state=filter_val,
    #     ).order_by(order)
    #     return new_context
    #
    # def get_context_data(self, **kwargs):
    #     context = super(MyView, self).get_context_data(**kwargs)
    #     context['filter'] = self.request.GET.get('filter', 'give-default-value')
    #     context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
    #     return context

def zakup_biletu(request, lot):
    imie = request.POST.get('imie', '')
    nazwisko = request.POST.get('nazwisko', '')

    with transaction.atomic():
        if lot.samolot.liczba_miejsc > lot.pasazerowie.all().count():
            pasazer = Pasazer(imie = imie, nazwisko = nazwisko)
            #pasazer.full_clean()
            pasazer.save()
            lot.pasazerowie.add(pasazer)

def szczegoly(request, lot_id):
    lot = get_object_or_404(Lot, pk=lot_id)
    samolot = get_object_or_404(Samolot, pk=lot.samolot.id)

    if request.method == "POST":
        zakup_biletu(request, lot)
        something_irrelevant = -1

    return HttpResponse(render(request, 'loty/szczegoly.html', locals()))

# class SzczegolyView(generic.DetailView):
#     model = Lot
#     template_name = 'loty/szczegoly.html'
#     context_object_name = 'lot'




#def showStuff(request):
#    loty = Lot.objects.all() # na stronie chcemy wyswietlic wszystkie obiekty tabeli Loty, wiec zapisujemy to do zmiennej
#    if request.method == 'POST':
#        form = LotForm(request.POST) # jezeli zostal wyslany formularz (czyli request HTTP POST) to tworzymy obiekt formularza z wpisanymi danymi
#        if form.is_valid(): # sprawdzamy poprawnosc wpisanych danych
#            form.save() # zapisujemy obiekt o danych przeslanych w formularzu do bazy danych
#            return HttpResponseRedirect('/') # dobra praktyka: przeladowujemy strone, aby po wcisnieciu F5 nie zostaly znowu wyslane dane, a pokazal sie ekran koncowy formularza (tutaj: zwykla strona)
#    else:
#        form = LotForm() # request HTTP GET, czyli nie zostal wyslany formularz - tworzymy obiekt niewypelnionego formularza
#    return render(request, 'loty.html', locals()) # bierzemy nasz request i slownik zmiennych lokalnych (w sumie interesuje nas aby mial klucze 'stuff' i 'form') i przesylamy go do szablonu HTML do przetworzenia i wyslania userowi
