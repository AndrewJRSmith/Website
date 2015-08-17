__author__ = 'ajrs'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()

from projects.models import Project
import datetime


def add_project(name, ongoing, startdate='', githuburl='', short_description='', more_info_button_text='', long_description=''):
    p = Project(name=name, ongoing=ongoing, short_description=short_description, more_info_button_text=more_info_button_text, long_description=long_description)

    if startdate:
        p.startdate = startdate
    if githuburl:
        p.githuburl = githuburl
    p.save()
    return p


def populate():
    website_proj = add_project(name='Website', ongoing=True,
                            short_description=
                                "I decided to make myself a website (this website) for several reasons. "
                                 "Firstly I wanted to learn how to as I had never delved into the world of "
                                 "web development before. Secondly I was interested in creating an "
                                 "interactive online scrapbook to document places I've been."
                               )

    urop_proj = add_project(name='MIT UROP', ongoing=False,
                            short_description=
                                "During the second semester of my year abroad at MIT I undertook a UROP "
                                "(Undergraduate Research Opportunity Project) with Caitlin Mueller "
                                "investigating new computational ways explore structural systems.",
                            long_description=
                                "<p>"
                                    "In a lecture at the start of the Fall Semester Caitlin Mueller demonstrated her online tool for structural optimisation and inspiration, <a href=""http://www.caitlinmueller.com/structurefit/"">StructureFit</a>."
                                    "This uses a multi-step genetic algorithm to produce variations on a structural design, aiming to increase both structural efficiency and aesthetics. "
                                    "I found this fascinating, and so started having hour-long weekly meetings with Caitlin to discuss my thoughts on the topic of structural engineering computation and optimisation. "
                                    "These then led to a UROP in the Spring Semester where I investigated computational techniques for better informing conceptual design. "
                                "</p>"
                            )

    collier_proj = add_project(name='Collier Memorial', ongoing=False,
                            short_description=
                                "Throughout my time at MIT I helped with the memorial to Sean Collier, "
                                "the MIT police office tragically killed in the aftermath of the Boston "
                                "Bombings.",
                            long_description =
                               "<p>"
                                    "Throughout the year I helped John Ochsendorf, an MIT professor, with several aspects of the Collier Memorial on the MIT campus. "
                                    "This is a five legged vaulted granite dome dedicated to the memory of the MIT police officer Sean Collier who was tragically killed in the aftermath of the Boston Bombings. "
                                    "My efforts on this project were particularly focused on the testing of materials and construction techniques. "
                                    "Early on we used large compression machines to investigate the mechanical properties of granite blocks along with the temporary plastic spacers that were placed in between. "
                                    "Then during the construction process I spearheaded age vs strength testing on the grout used to fill the gaps between the stones to assess the implications of reducing the ageing time before loading. "
                                    "I also helped design, test and implement the method for checking how much arching action had developed while lowering the granite stones and helped collect the data on the day of the lowering. "
                                    "During the process I also carried out various other small tasks such as a basic thermal expansion analysis. "
                                "</p>")

    iass_pavilion = add_project(name='IASS 2015 Pavilion', ongoing=False,
                            short_description=
                                "I helped design and construct a structural engineering art exhibition "
                                "piece for the 2015 IASS in Amsterdam. This team was headed by Caitlin "
                                "Mueller and contained several members of MIT's Building Technology "
                                "Group",
                            long_description=
                                "<p>"
                                    "In the Spring Semester Caitlin Mueller announced that she wanted to enter a competition being held as part of the International Annual Structures Symposium (IASS) conference in 2015. "
                                    "Teams from around the world were invited to design an architectural sculpture to be displayed in Amsterdam for the two months prior to the conference. "
                                    "I had never had the chance to do something like this before so I jumped at the opportunity and helped the team finalise the design throughout the semester. "
                                    "We decided to produce a set of 6m high pre-tensioned arches which all started at the same point on the ground and ended at the same point on a wall but gradually had a stronger and stronger inflection point half way up, such that when combined it looked like undulating waves. "
                                    "This was based on previous work by Leonardo .... who wrote a script that produces post-tensioning solutions to stabilise discretised curves. "
                                    "There were tight restrictions on weight and volume of materials, so we decided to laser-print stencils onto corrugated cardboard for folding into boxes on-site. "
                                    "Cardboard tubes and straps were then used for the post-tensioning system. "
                                    "As part of my contribution I helped design and construct LED lighting strips to be fitting to the arches, illuminating the underside of the boxes. "
                                "</p>")

    # Print out what we have added to the user.
    for p in Project.objects.all():
        print(p)


# Start execution here!
if __name__ == '__main__':
    print("Starting Projects population script...")
    Project.objects.all().delete()
    populate()