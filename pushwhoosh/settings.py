'''
Created on 20 Aug 2014

@author: michael
'''
from django.conf import settings

PUSHWHOOSH_ACCESS_TOKEN = getattr(settings, 'PUSHWHOOSH_ACCESS_TOKEN', None)
PUSHWHOOSH_GROUP_CODE = getattr(settings, 'PUSHWHOOSH_GROUP_CODE', None)
PUSHWHOOSH_APPLICATION_CODE = getattr(settings, 'PUSHWHOOSH_APPLICATION_CODE', None)
PUSHWHOOSH_LOG_API_CALLS = getattr(settings, 'PUSHWHOOSH_LOG_API_CALLS', True)