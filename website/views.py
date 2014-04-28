from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from website.models import *

# Create your views here.
def index(request):
    return render(request, 'website/index.html', {})

def work(request):
    return render(request, 'website/work.html', {})

def me(request):
    return render(request, 'website/me.html', {})

def resume_html(request):
	return render(request, 'website/resume.html', {})

