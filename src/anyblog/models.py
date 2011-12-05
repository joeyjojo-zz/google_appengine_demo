from django.db import models
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    timestampcreated = models.DateTimeField(auto_now_add=True)
    timestampmodified = models.DateTimeField(auto_now=True)
    yearmonth = models.ForeignKey('ArchiveYearMonth', null=True)


    def __init__(self, *args, **kwargs):
        super(BlogPost, self).__init__(*args, **kwargs)
        # search the Archive to see if the year/month has been added
        if self.timestampcreated is not None:
            q = ArchiveYearMonth.objects.filter(year__exact=self.timestampcreated.year)\
                                        .filter(month__exact=self.timestampcreated.month)
            try:
                res = q.get()
                self.yearmonth = res
            except ObjectDoesNotExist as e:
                ymo = ArchiveYearMonth(year=self.timestampcreated.year,
                                       month=self.timestampcreated.month)
                ymo.save()
                self.yearmonth = ymo

    def __unicode__(self):
        return u"<BlogPost (title={0}, content={1}, author={2}, created={3}, modified={4})>".format(
            self.title,
            self.content,
            self.author,
            self.timestampcreated,
            self.timestampmodified
        )


class ArchiveYearMonth(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()

    def __unicode__(self):
        return u"<ArchiveYearMonth ({0}-{1})>".format(self.year,
                                                      self.month)