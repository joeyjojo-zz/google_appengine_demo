# Create your views here.
import collections

from django.shortcuts import render_to_response

import models

def index(request):
    latest_blog_list = models.BlogPost.objects.all().order_by('-timestampcreated')[:5]
    year_month_objects = models.ArchiveYearMonth.objects.all().order_by("-year").order_by("-month")
    d = collections.OrderedDict()

    year_month_list = [(2011,["January", "March", "October",],),(2010,["February", "March", "April",],),]

    #print year_month_objects
    # TODO: Cut this down to the first 100 chars of post
    return render_to_response('index.html', {'latest_blog_list': latest_blog_list,
                                             'year_month_list': year_month_list})

def detail(request):
    # TODO: make this right
    return render_to_response('index.html')