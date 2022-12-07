from django.contrib import admin
from about.models import ProfessionalExperience, ProfileEducation, ProfileCertification


# Register your models here.


@admin.register(ProfessionalExperience)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'position',)


@admin.register(ProfileEducation)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'institution', 'course',)


@admin.register(ProfileCertification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('user', "institution", 'course',)
