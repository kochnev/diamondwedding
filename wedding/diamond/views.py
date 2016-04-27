from django.shortcuts import render

def index(request):
    return render(request, 'diamond/index.html', {})

def about(request):
    return render(request, 'diamond/about.html', {})

def contacts(request):
    return render(request, 'diamond/contacts.html', {})

def testimonials(request):
    return render(request, 'diamond/testimonials.html', {})
