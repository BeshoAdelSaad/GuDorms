from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request,'index.html', context)

def about(request):
    context = {

    }
    return render(request,'Pages/about.html', context)

def contact(request):
    context = {

    }
    return render(request,'Pages/contact.html', context)

