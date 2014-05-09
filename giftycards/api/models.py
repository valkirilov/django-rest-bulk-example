# Create your models here.
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    degree = models.CharField(max_length=90, null=False, blank=False)
    short = models.CharField(max_length=5, null=False, blank=False)
    email = models.EmailField()
    department = models.CharField(max_length=10)
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True)
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True)
        
    # def __unicode__(self):
    #     return (u'%(name)s %(degree)s %(short)s') % dict(
    #         name=self.name,
    #         degree=self.degree,
    #         short=self.short,
    #         )