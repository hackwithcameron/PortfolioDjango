from django.shortcuts import render


def handler404(request, ex):
    return render(request, 'ErrorHandling/404.html', status=404)


def handler500(request):
    return render(request, 'ErrorHandling/404.html', status=500)
