from django.shortcuts import render

# Create your views here.
def projects(request):
    context_dict = []
    return render(request, 'projects/projects.html', context_dict)