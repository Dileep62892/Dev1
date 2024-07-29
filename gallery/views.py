from django.shortcuts import render
import os
from django.conf import settings

def index(request):
    projects = [d for d in os.listdir(settings.MEDIA_ROOT) if os.path.isdir(os.path.join(settings.MEDIA_ROOT, d))]
    return render(request, 'gallery/index.html', {'projects': projects})

def project_view(request, project_name):
    project_path = os.path.join(settings.MEDIA_ROOT, project_name)
    images = [f for f in os.listdir(project_path) if os.path.isfile(os.path.join(project_path, f))]
    image_urls = [os.path.join(settings.MEDIA_URL, project_name, image) for image in images]
    return render(request, 'gallery/carousel.html', {'project_name': project_name, 'images': image_urls})
