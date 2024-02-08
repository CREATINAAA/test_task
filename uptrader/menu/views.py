from django.shortcuts import render

def menu(request, *args, **kwargs):
    return render(request, 'index.html')    
