from django.db import models

# Create your models here.
class FetchInterestingUrl(models.Model):
    url = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    status = models.IntegerField()
    class Meta:
        db_table = 'interesting_url'


class FetchNonInterestingUrl(models.Model):
    url = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    class Meta:
        db_table = 'non_interesting_url'

class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'


class Admin(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    class Meta:
        db_table = 'admin'