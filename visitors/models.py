from django.db import models

class Visitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    call_sign = models.CharField(max_length=10)
    nfarl_member = models.BooleanField()
    contact_me = models.BooleanField()
    email = models.CharField(max_length=50)
    first_time = models.BooleanField()
    age = models.PositiveSmallIntegerField()

