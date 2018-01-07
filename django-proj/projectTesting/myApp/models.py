from django.db import models

# Create your models here.
class Topic(models.Model):
    top_Name = models.CharField(max_length=264)

    def __str__(self):
        return self.top_Name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
