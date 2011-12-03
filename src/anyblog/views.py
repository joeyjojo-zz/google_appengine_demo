# Create your views here.
from django.shortcuts import render_to_response
import models

def index(request):
    latest_blog_list = models.BlogPost.objects.all().order_by('-timestampcreated')[:5]
    return render_to_response('anyblog/index.html', {'latest_blog_list': latest_blog_list})
