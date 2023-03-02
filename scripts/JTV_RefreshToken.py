#! /usr/bin/python3

import requests



    sUrl = "https://auth.media.jio.com/tokenservice/apis/v1/refreshtoken"
    body = {
    "refreshToken":"c1df31fd-4866-4c02-bd8e-508dc9df3696",
    "devicetype" : "phone",
    "versionCode" : 290,
    "os" : "android",
    "appName": "RJIL_JioTV",
    "deviceId" : "3c6d6b5702fa09bd"
    }
    r = requests.post(url = sUrl, data = body).text
    print(f'"{r}"')

