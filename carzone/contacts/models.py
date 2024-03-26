from datetime import datetime

from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    car_id = models.IntegerField()
    customer_need = models.CharField(
        max_length=50,
    )
    car_title = models.CharField(
        max_length=50,
    )
    city = models.CharField(
        max_length=50,
    )
    state = models.CharField(
        max_length=50,
    )
    email = models.EmailField()
    phone = models.CharField(
        max_length=50,
    )
    message = models.TextField(
        blank=True,
    )
    user_id = models.IntegerField(
        blank=True,
    )
    create_date = models.DateTimeField(
        blank=True,
        default=datetime.now(),
    )

    def __str__(self):
        return self.email
