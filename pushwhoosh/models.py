'''
Created on 20 Aug 2014

@author: michael
'''
import uuid

from django.db import models

from pushwhoosh import constants


class PushWhooshNotification(models.Model):
    uuid = models.CharField(max_length=255)
    request_data = models.TextField()
    request_data = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    api_method = models.PositiveSmallIntegerField(
        choices=constants.API_METHOD_CHOICES
    )

    def __unicode__(self):
        return u'%s' % self.uuid

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid.uuid4()
        super(PushWhooshNotification).save(*args, **kwargs)
