from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = []
    return render(request, 'basic_pages/index.html', context_dict)


def about(request):
    context_dict = []
    return render(request, 'basic_pages/about.html', context_dict)


def contact(request):
    context_dict = []
    return render(request, 'basic_pages/contact.html', context_dict)


def music(request):
    context_dict = []
    return render(request, 'basic_pages/music.html', context_dict)


def projects(request):
    context_dict = []
    return render(request, 'basic_pages/projects.html', context_dict)


def scrapbook(request):
    context_dict = []
    return render(request, 'basic_pages/scrapbook.html', context_dict)


def structuralengineering(request):
    context_dict = []
    return render(request, 'basic_pages/structuralengineering.html', context_dict)