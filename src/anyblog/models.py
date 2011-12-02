from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    timestampcreated = models.DateTimeField(auto_now_add=True)
    timestampmodified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"<BlogPost (title={0}, content={1}, author={2}, created={3}, modified={4})>".format(
            self.title,
            self.content,
            self.author,
            self.timestampcreated,
            self.timestampmodified
        )