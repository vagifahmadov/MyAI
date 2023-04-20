from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    desc = models.TextField(max_length=290)

    class Meta:
        db_table = 'ai_services'

    def __str__(self):
        return self.name


class Pages(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=80)
    body = models.TextField()

    class Meta:
        db_table = 'web_pages'

    def __str__(self):
        return self.name
