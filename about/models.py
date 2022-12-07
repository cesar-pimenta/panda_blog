from django.db import models
from core.mixins import DateCreateUpdate
from perfil.models import Profile


class ProfessionalExperience(DateCreateUpdate):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='professionalExperience')
    company = models.CharField(max_length=256, null=True, blank=True)
    position = models.CharField(max_length=256, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    final_date = models.DateField(null=True, blank=True)
    resume = models.TextField(null=True, blank=True)
    is_working = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Professional Experience'
        verbose_name_plural = 'Professional Experiences'

    def __str__(self):
        return '{} - in -> {}'.format(self.position, self.company)
