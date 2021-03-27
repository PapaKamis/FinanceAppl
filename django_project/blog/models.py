from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from adaptor.model import CsvModel
# from adaptor.fields import DateField, FloatField, IntegerField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Hist(models.Model):
    Date = models.DateField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()
    AdjClose = models.FloatField()
    Volume = models.IntegerField()

#
#     class Meta:
#         delimeter = ","



# python manage.py shell
# user = User.objects.get(id=1), filter, first, all
# Post.objects.all(), post_1.save()

#