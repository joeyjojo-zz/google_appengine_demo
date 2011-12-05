# Create your views here.
import collections
import logging
import datetime

from django.shortcuts import render_to_response

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
        d[ym.year].append(dt.strftime('%B'))
    # send to the view
    return render_to_response('index.html', {'latest_blog_list': latest_blog_list,
                                             'year_month_dict': d})

def detail(request, blogpost_id):
    """
    Returns the template for an idividual blog post
    @param blogpost_id: The id of the blog post to display
    @type blogpost_id: int
    """
    # TODO: make this right
    return render_to_response('index.html')

def month_archive(request, year, month):
    """
    Returns an archive view for all the blogposts against that year/month
    @param year: The year of the blog posts to display
    @type year: int
    @param month: The month of the blog posts to display
    @type month: int
    """
    # TODO: make this right
    return render_to_response('index.html')