# Create your views here.
import collections
import logging
import datetime
import calendar
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers

import models

logger = logging.getLogger(__name__)

def index(request):
    """
    Returns the template for the main page.
    """
    # get the blogs we need
    # TODO: Cut this down to the first 100 chars of post
    latest_blog_list = models.BlogPost.objects.all().order_by('-timestampcreated')[:5]
    # get the archive data
    year_month_objects = models.ArchiveYearMonth.objects.all().order_by("-year").order_by("-month")
    # put it into the format we need
    d = collections.OrderedDict()
    for ym in year_month_objects:
        dt = datetime.date(ym.year, ym.month, 1)
        if ym.year not in d:
            d[ym.year] = []
        d[ym.year].append({"id":ym.month, "name":dt.strftime('%B')})
    # send to the view
    return render_to_response('index.html', {'latest_blog_list': latest_blog_list,
                                             'year_month_dict': d})

def detail(request, blogpost_id):
    """
    Returns the template for an individual blog post
    @param blogpost_id: The id of the blog post to display
    @type blogpost_id: int
    """
    blog_list = [models.BlogPost.objects.get(id=blogpost_id),]
    return render_to_response('detail.html', {'latest_blog_list':blog_list})

def month_archive(request, year, month):
    """
    Returns an archive view for all the blogposts against that year/month
    @param year: The year of the blog posts to display
    @type year: int
    @param month: The month of the blog posts to display
    @type month: int
    """
    year = int(year)
    month = int(month)
    minday, maxday = calendar.monthrange(year, month)
    mintimestamp = datetime.datetime(year, month, minday)
    maxtimestamp = datetime.datetime(year, month, maxday)
    blog_list = models.BlogPost.objects.all().filter(timestampcreated__gt=mintimestamp)\
                                             .filter(timestampcreated__lt=maxtimestamp)
    return render_to_response('detail.html', {'latest_blog_list':blog_list})

def get_next_results(request, num_to_retrieve, current_index):
    """
    Returns the next 5 blog posts as a json object
    """
    if request.is_ajax():
        current_index = int(current_index)
        num_to_retrieve = int(num_to_retrieve)
        latest_blog_list = models.BlogPost.objects.all().order_by('-timestampcreated')[current_index:current_index+num_to_retrieve]
        json_serializer = serializers.get_serializer("json")()
        json = json_serializer.serialize(latest_blog_list, ensure_ascii=False)
        return HttpResponse(json, mimetype='application/json')

