from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class AgriculturalEquipment(models.Model):
    equipment_name = models.CharField(max_length=200,)
    equipment_description = HTMLField()