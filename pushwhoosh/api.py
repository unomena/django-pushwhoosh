'''
Created on 20 Aug 2014

@author: michael
'''
import json

from django.conf import settings

import requests

from pushwhoosh import models, constants

SERVICE_URL = 'https://cp.pushwoosh.com/json/1.3/%s'


def create_message(notifications, use_applications_group=False):
    request_data = {
         "auth": settings.PUSHWHOOSH_ACCESS_TOKEN,
         "notifications": notifications
    }
    if use_applications_group:
        request_data.update({
            "applications_group": settings.PUSHWHOOSH_GROUP_CODE
        })
    else:
        request_data.update({
            "application": settings.PUSHWHOOSH_APPLICATION_CODE
        })
    data = json.dumps({
        "request": request_data
    })
    response = requests.post(
        SERVICE_URL % "createMessage",
        data=data
    )
    models.PushWhooshNotification.objects.create(
        api_method=constants.API_METHOD_CREATE_MESSAGE,
        request_data=data,
        respose_data=response.json()
    )
    return response


def delete_message(message_code):
    data = json.dumps({
        "request": {
            "auth": settings.PUSHWHOOSH_ACCESS_TOKEN,
            "message": message_code
        }
    })
    response = requests.post(
        SERVICE_URL % "deleteMessage",
        data=data
    )
    models.PushWhooshNotification.objects.create(
        api_method=constants.API_METHOD_DELETE_MESSAGE,
        request_data=data,
        respose_data=response.json()
    )
    return response
