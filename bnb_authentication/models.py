from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class UserRegistration(models.Model):
   
    phone_regex = RegexValidator( regex = r'^\+?1?\d{9,14}$')
    phone = models.CharField(validators = [phone_regex], max_length=17)
    otp = models.CharField(max_length=9, blank=True, null=True)
    validated = models.BooleanField(default=False, help_text= 'if it is true, that means user have validate opt correctly in seconds')
    first_name = models.CharField(max_length=254, blank=True, null=True)
    last_name = models.CharField(max_length=254, blank=True, null=True)
    date_of_birth = models.DateField(max_length=8, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.phone
        