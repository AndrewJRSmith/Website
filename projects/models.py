from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    ongoing = models.BooleanField(default=True)
    start_date = models.DateField(null=True, verbose_name='Start Date', blank=True)
    github_url = models.URLField(null=True, verbose_name='GitHub URL', blank=True)
    description = models.TextField(default='')
    more_info = models.CharField(max_length=20, blank=True,
                                 verbose_name='More Information Page Name')

    def __str__(self):
        return self.name
