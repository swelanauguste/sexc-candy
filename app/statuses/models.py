from django.db import models


class Status(models.Model):
    uid = models.CharField("NIC", max_length=6, blank=True, null=True)
    name = models.CharField(max_length=255)
    received = models.DateField()
    expires = models.DateField()
    
    class Meta:
        ordering = ('-expires',)

    def __str__(self):
        return self.name
