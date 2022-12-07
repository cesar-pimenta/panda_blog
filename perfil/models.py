from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, related_name='userprofile',
                                editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)
    lastName = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{} {}'.format(self.name, self.lastName)
