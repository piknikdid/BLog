# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog_Post(models.Model):
    title = models.CharField(max_length=40)
    blog_text = models.TextField(max_length=400)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
