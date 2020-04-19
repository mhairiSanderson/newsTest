from django.db import models


class Story(models.Model):
    heading_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')
    content_text = models.CharField(max_length=700)
    def __str__(self):
        return self.heading_text

