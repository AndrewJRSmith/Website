from django.shortcuts import render
from projects.models import Project


# Create your views here.
def projects(request):
    projects_list = Project.objects.order_by('-ongoing', '-start_date')
    context_dict = {'Projects': projects_list}
    return render(request, 'projects/projects.html', context_dict)


def more_info(request, more_info_page):
    context_dict = []
    return render(request, 'projects/more_info/{0}.html'.format(more_info_page), context_dict)
