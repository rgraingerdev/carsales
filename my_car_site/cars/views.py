from django.shortcuts import render

def list(request):
    # Your view logic here
    return render(request, 'list.html')

def add(request):
    # Your view logic here
    return render(request, 'add.html')

def delete(request):
    # Your view logic here
    return render(request, 'delete.html')