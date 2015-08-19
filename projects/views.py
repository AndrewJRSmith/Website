from django.shortcuts import render
from projects.models import Project, ProjectImage


# Create your views here.
def projects(request):
    projects_list = Project.objects.order_by('-ongoing', '-start_date')
    projects_images_list = ProjectImage.objects.order_by('order_id')

    for project in projects_list:
        if project.long_description and ProjectImage.objects.filter(project=project):
            project.more_info_button_text = 'More info and project images'
            project.images_exist = True
        elif project.long_description:
            project.more_info_button_text = 'More info'
        elif ProjectImage.objects.filter(project = project):
            project.more_info_button_text = 'Project images'
            project.images_exist = True
        else:
            project.more_info_button_text = ''

    context_dict = {'Projects': projects_list,
                    'ProjectImages': projects_images_list}

    return render(request, 'projects/projects.html', context_dict)


def more_info(request, more_info_page):
    context_dict = []
    return render(request, 'projects/more_info/{0}.html'.format(more_info_page), context_dict)
