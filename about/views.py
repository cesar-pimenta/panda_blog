from django.shortcuts import render, HttpResponse
from perfil.models import Profile


def index(request):
    profile = Profile.objects.last()
    return render(request, 'about/index.html', context={
        "profile": profile,
    })
