from django.db import models
from platform import architecture

class mlModels(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    architecture = models.FileField(upload_to= 'mlmodels/')
    weigths = models.FileField(upload_to = 'mlmodels/')
    priority = models.PositiveSmallIntegerField(null=True)