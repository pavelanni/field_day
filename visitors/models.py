from django.db import models

class Visitor(models.Model):
    AGE_CHOICES = (
        (0, '<10'),
        (10, '10-20'),
        (20, '21-30'),
        (30, '31-40'),
        (40, '41-50'),
        (50, '51-60'),
        (60, '61-70'),
        (70, '71-80'),
        (80, '>=81'),
        (100, 'Don\'t ask!')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    call_sign = models.SlugField(max_length=10)
    nfarl_member = models.BooleanField()
    contact_me = models.BooleanField()
    email = models.EmailField()
    first_time = models.BooleanField()
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES, default=100,)

    def __str__(self):
        return self.last_name

