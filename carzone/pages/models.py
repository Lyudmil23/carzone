from django.db import models


class Team(models.Model):
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    designation = models.CharField(
        max_length=100,
    )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    google_plus_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name