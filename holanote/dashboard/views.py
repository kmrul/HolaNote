from django.shortcuts import render

def dashboard(request):
    return render(request, 'templates/dashboard/dashboard.html')
