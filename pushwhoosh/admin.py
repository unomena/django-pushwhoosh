'''
Created on 20 Aug 2014

@author: michael
'''
from django.contrib import admin

from pushwhoosh import models


class PushWhooshNotificationAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'uuid', 'api_method')
    list_filter = ('timestamp', 'api_method')

admin.site.register(models.PushWhooshNotification, PushWhooshNotificationAdmin)
