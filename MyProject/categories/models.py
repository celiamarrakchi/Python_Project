from django.db import models
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError
# Create your models here.
def validate_letters_only(value):
    if not re.match(r'^[A-Za-z\s]+$',value):
        raise ValidationError('This field should only containt letters.')
class Category(models.Model):
    letters_only=RegexValidator(r'^[A-Za-z\s]+$','Only letters are allowed')
    title=models.CharField(max_length=255,validators=[validate_letters_only])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="Categories"