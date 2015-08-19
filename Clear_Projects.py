__author__ = 'ajrs'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()

from projects.models import Project

# Start execution here!
if __name__ == '__main__':
    print("Starting Project clearing script...")
    Project.objects.all().delete()