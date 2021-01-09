from django.db import models
from accounts.models import MyUser
from django.core.validators import RegexValidator

class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class State(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    phone_regex = RegexValidator(
        regex=r'^(?:\s+|)((0|(?:(\+|)91))(?:\s|-)*(?:(?:\d(?:\s|-)*\d{9})|(?:\d{2}(?:\s|-)*\d{8})|(?:\d{3}(?:\s|-)*\d{7}))|\d{10})(?:\s+|)$',
        message="Phone number entered must be in a valid format.")
    phone = models.CharField(validators=[phone_regex], max_length=15)
