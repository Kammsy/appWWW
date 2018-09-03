#coding=utf-8

from django.db import models

class Pasazer(models.Model):
    imie = models.CharField(max_length=42)
    nazwisko = models.CharField(max_length=42)

    #class Meta:
    #    unique_together = (('imie', 'nazwisko'),)

class Samolot(models.Model):
    znaki_rejestracyjne = models.CharField(max_length=100)
    #znaki_rejestracyjne = models.CharField(max_length=50, unique=True)
    liczba_miejsc = models.IntegerField()

class Lot(models.Model):
    lotnisko_startu = models.CharField(max_length=100)
    czas_startu = models.DateTimeField()
    lotnisko_ladowania = models.CharField(max_length=100)
    czas_ladowania = models.DateTimeField()
    samolot = models.ForeignKey(Samolot, on_delete=models.CASCADE)
    pasazerowie = models.ManyToManyField(Pasazer)

#class Bilet(models.Model):
#    pasazer
