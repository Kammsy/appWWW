from django.core.management.base import BaseCommand

from random import choice, randint
from string import ascii_uppercase
from datetime import datetime, timedelta

from loty.models import Pasazer, Lot, Samolot

class Command(BaseCommand):
	def _zapisz_dane(self):
		czas = datetime(year=2018, month=8, day=1, hour=11, minute=30, tzinfo=<UTC>)

		for i in range(60):
			nowySamolot = Samolot(znaki_rejestracyjne=''.join(choice(ascii_uppercase) for i in range(10)), liczba_miejsc=randint(30,100))

			nowySamolot.save()

			for j in range(60):
				lot = Lot(lotnisko_startu='WAW', czas_startu=czas, lotnisko_ladowania='KRK', czas_ladowania=czas+timedelta(hours=1), samolot=nowySamolot)

				lot.save()

				czas += timedelta(days=1)

	def handle(self, *args, **options):
		self._zapisz_dane()
