from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=300, null=False)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250)


