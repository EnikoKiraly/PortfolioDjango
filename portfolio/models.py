from django.db import models

# Create your models here.

class Skil(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Timeline(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    year_start = models.CharField(max_length=4, null=True)
    year_finish = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.company_name


class Project(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='project_foto/')
    github = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to='certificate_foto/')

    def __str__(self):
        return self.title