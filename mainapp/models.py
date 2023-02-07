from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

def form_validator(value):
    if value[0] != 's':
        raise models.ValidationError('Name should start with s')

class User(models.Model):
    name=models.CharField(max_length=70)
    contact=models.CharField(max_length=100,validators=[RegexValidator(r'^(?:\+88|88)?(01[3-9]\d{8})$', message="Phone number is not valid")])


