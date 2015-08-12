__author__ = 'ajrs'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()

from projects.models import Project
import datetime


def add_project(name, ongoing, startdate='', githuburl='', description='', more_info=''):
    p = Project(name=name, ongoing=ongoing, description=description, more_info=more_info)

    if startdate:
        p.startdate = startdate
    if githuburl:
        p.githuburl = githuburl
    p.save()
    return p


def populate():
    website_proj = add_project(name='Website', ongoing=True,
                               description="I decided to make myself a website (this website) for several reasons. "
                                           "Firstly I wanted to learn how to as I had never delved into the world of "
                                           "web development before. Secondly I was interested in creating an "
                                           "interactive online scrapbook to document places I've been.",
                               more_info='website')

    urop_proj = add_project(name='MIT UROP', ongoing=False,
                            description="During the second semester of my year abroad at MIT I undertook a UROP "
                                        "(Undergraduate Research Opportunity Project) with Caitlin Mueller "
                                        "investigating new computational ways explore structural systems.",
                            more_info='urop')

    collier_proj = add_project(name='Collier Memorial', ongoing=False,
                               description="Throughout my time at MIT I helped with the memorial to Sean Collier, "
                                           "the MIT police office tragically killed in the aftermath of the Boston "
                                           "Bombings.")

    iass_pavilion = add_project(name='IASS 2015 Pavilion', ongoing=False,
                                description="I helped design and construct a structural engineering art exhibition "
                                            "piece for the 2015 IASS in Amsterdam. This team was headed by Caitlin "
                                            "Mueller and contained several members of MIT's Building Technology "
                                            "Group")

    # Print out what we have added to the user.
    for p in Project.objects.all():
        print(p)


# Start execution here!
if __name__ == '__main__':
    print("Starting Projects population script...")
    Project.objects.all().delete()
    populate()