'''
Created on 20 Aug 2014

@author: michael
'''
import json

import requests

from pushwhoosh import models, constants, settings

SERVICE_URL = 'https://cp.pushwoosh.com/json/1.3/%s'


def _log_api_call(api_method, request_data, response_data):
    models.PushWhooshNotification.objects.create(
        api_method=api_method,
        request_data=request_data,
        respose_data=response_data
    )


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
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_CREATE_MESSAGE,
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
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_DELETE_MESSAGE,
            request_data=data,
            respose_data=response.json()
        )
    return response


def register_device(device_push_token, hwid, timezone_offset_seconds,
                    device_type, language="en"):
    data = json.dumps({
        "request": {
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "push_token": device_push_token,
            "language": language,
            "hwid": hwid,
            "timezone": timezone_offset_seconds,
            "device_type": device_type
        }
    })
    response = requests.post(
        SERVICE_URL % "registerDevice",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_REGISTER_DEVICE,
            request_data=data,
            respose_data=response.json()
        )
    return response


def unregister_device(hwid):
    data = json.dumps({
        "request": {
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "hwid": hwid,
        }
    })
    response = requests.post(
        SERVICE_URL % "unregisterDevice",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_UNREGISTER_DEVICE,
            request_data=data,
            respose_data=response.json()
        )
    return response


def set_tags(hwid, tags):
    data = json.dumps({
        "request": {
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "hwid": hwid,
            "tags": tags
        }
    })
    response = requests.post(
        SERVICE_URL % "setTags",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_SET_TAGS,
            request_data=data,
            respose_data=response.json()
        )
    return response


def get_tags(hwid):
    data = json.dumps({
        "request": {
            "auth": settings.PUSHWHOOSH_ACCESS_TOKEN,
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "hwid": hwid,
        }
    })
    response = requests.post(
        SERVICE_URL % "getTags",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_GET_TAGS,
            request_data=data,
            respose_data=response.json()
        )
    return response


def set_badge(hwid, badge):
    data = json.dumps({
        "request": {
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "hwid": hwid,
            "badge": badge
        }
    })
    response = requests.post(
        SERVICE_URL % "setBadge",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_SET_BADGE,
            request_data=data,
            respose_data=response.json()
        )
    return response


def push_stat(hwid, notification_hash):
    data = json.dumps({
        "request": {
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "hwid": hwid,
            "hash": notification_hash
        }
    })
    response = requests.post(
        SERVICE_URL % "pushStat",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_PUSH_STAT,
            request_data=data,
            respose_data=response.json()
        )
    return response


def get_nearest_zone(hwid, latitude, longitude):
    data = json.dumps({
        "request": {
            "application": settings.PUSHWHOOSH_APPLICATION_CODE,
            "hwid": hwid,
            "lat": latitude,
            "long": longitude
        }
    })
    response = requests.post(
        SERVICE_URL % "getNearestZone",
        data=data
    )
    if settings.PUSHWHOOSH_LOG_API_CALLS:
        _log_api_call(
            constants.API_METHOD_GET_NEAREST_ZONE,
            request_data=data,
            respose_data=response.json()
        )
    return response
