from django.shortcuts import render

def home(request):
    return render(request, 'Projects/projectsHome.html')


