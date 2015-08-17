from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    ongoing = models.BooleanField(default=True)
    start_date = models.DateField(null=True, verbose_name='Start Date', blank=True)
    github_url = models.URLField(null=True, verbose_name='GitHub URL', blank=True)
    short_description = models.TextField(blank=True, null=True, verbose_name='Short Description')
    long_description = models.TextField(blank=True, null=True, verbose_name='Long Description')
    more_info_button_text = models.CharField(max_length=30, blank=True, verbose_name='More Info Button Text')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.long_description and ProjectImage.objects.filter(project = self):
            self.more_info_button_text = 'More info and project images'
        elif self.long_description:
            self.more_info_button_text = 'More info'
        elif ProjectImage.objects.filter(project = self):
            self.more_info_button_text = 'Project images'
        else:
            self.more_info_button_text = ''
        super(Project, self).save(*args, **kwargs)



class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField(upload_to='project_images', blank=False)
    caption = models.TextField(blank=True, null=True)