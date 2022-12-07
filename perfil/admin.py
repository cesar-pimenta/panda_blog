from django.contrib import admin
from perfil.models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastName', )
    list_filter = ('name', )
    search_fields = ['name', 'lastName']
