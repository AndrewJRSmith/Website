from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ongoing = models.BooleanField(default=True)
    start_date = models.DateField(null=True, verbose_name='Start Date', blank=True)
    github_url = models.URLField(null=True, verbose_name='GitHub URL', blank=True)
    short_description = models.TextField(blank=True, null=True, verbose_name='Short Description')
    long_description = models.TextField(blank=True, null=True, verbose_name='Long Description')
    more_info_button_text = models.CharField(max_length=30, blank=True, verbose_name='More Info Button Text')
    slug = models.SlugField(unique=True)
    images_exist = models.BooleanField(default=False)


    def display_long_description(self):
        return mark_safe(self.long_description)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField(upload_to='project_images', blank=False)
    caption = models.TextField(blank=True, null=True)
    order_id = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.project.name + " - " + self.order_id.__str__()
