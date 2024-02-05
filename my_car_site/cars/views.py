from django.shortcuts import render

# Create your views here.
def list(request):
    return(render, 'cars/list.html')

def add(request):
    return(render, 'cars/add.html')

def delete(request):
    return(render, 'cars/delete.html')