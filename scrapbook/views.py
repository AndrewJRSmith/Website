from django.shortcuts import render


# Create your views here.
def scrapbook(request):
    context_dict = []
    return render(request, 'scrapbook/scrapbook.html', context_dict)
