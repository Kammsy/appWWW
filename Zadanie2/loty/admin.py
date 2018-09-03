from django.contrib import admin
from loty.models import Pasazer, Samolot, Lot

# ponizsze rejestruje model w panelu administracyjnym. jest to konieczne by sie model w ogole w nim pojawil.
class PasazerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pasazer, PasazerAdmin)

class SamolotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Samolot, SamolotAdmin)

class LotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lot, LotAdmin)
