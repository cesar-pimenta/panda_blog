from django.db import models


class DateCreateUpdate(models.Model):
    date_create = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, editable=True)
    date_update = models.DateTimeField(auto_now=True, null=True, editable=True)

    class Meta:
        abstract = True
