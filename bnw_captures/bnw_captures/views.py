from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def explore(request):
    return render(request,'explore.html')

def illusion(request):
    return render(request,'story1.html')

def abstract(request):
    return render(request, 'story2.html')

def mandala(request):
    return render(request, 'story3.html')

def gothic(request):
    return render(request, 'story4.html')

def macabre(request):
    return render(request, 'story5.html')

def loop(request):
    return render(request, 'story6.html')

def manuscript(request):
    return render(request, 'story7.html')

def ghoul(request):
    return render(request, 'story8.html')

def darknet(request):
    return render(request, 'story9.html')

def ai(request):
    return render(request, 'story10.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')