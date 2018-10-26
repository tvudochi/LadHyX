from django.contrib import admin
from personnel.models import Personnel, Bureau, Telephone, Email

# Register your models here.


class PersonnelAdmin(admin.ModelAdmin):
    list_display = (
        'personnel_id', 'nom', 'prenom', 'categorie',
        'fonction', 'page_perso', 'Photo'
    )
    ordering = ['nom']


admin.site.register(Personnel, PersonnelAdmin)

admin.site.register(Bureau)
admin.site.register(Telephone)
admin.site.register(Email)
