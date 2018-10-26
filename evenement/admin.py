from django.contrib import admin
from evenement.models import Evenement

# Register your models here.


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('intitule_id', 'intitule', 'type', 'personne',
                    'date_debut', 'date_fin', 'lieu')

admin.site.register(Evenement, EvenementAdmin)
