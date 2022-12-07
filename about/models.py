import datetime
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

    def duration(self):
        if self.final_date:
            duration = (self.final_date - self.start_date)
            return duration.days
        else:
            duration = (datetime.date.today() - self.start_date)
            return duration.days


class ProfileEducation(DateCreateUpdate):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=256, null=True, blank=True)
    course = models.CharField(max_length=256, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    final_date = models.DateField(null=True, blank=True)
    resume = models.TextField(null=True, blank=True)
    is_studying = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-final_date']

    def __str__(self):
        return '{} - in -> {}'.format(self.course, self.institution)


class ProfileCertification(DateCreateUpdate):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certification')
    institution = models.CharField(max_length=256, null=True, blank=True)
    course = models.CharField(max_length=256, null=True, blank=True)
    year = models.DateField(null=True, blank=True)
    resume = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return '{} - in -> {}'.format(self.course, self.institution)