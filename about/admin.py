from django.contrib import admin
from about.models import ProfessionalExperience
# Register your models here.


@admin.register(ProfessionalExperience)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'position', )
