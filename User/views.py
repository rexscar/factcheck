from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json


# Create your views here.
@api_view(['POST'])
def getUserData(request) :
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['code']
    print(content)
    header = {'content-Type': 'application/x-www-form-urlencoded'}

    api_body = {
        "code": content,
        "grant_type": "authorization_code",
        "client_id": "aXpOOWZkSm1JVHJ3S0o3YkJhSmI6MTpjaQ",
        "redirect_uri": "https://twitterfactchecker.herokuapp.com/callback",
        "code_verifier": "challenge"
    }
    payload = json.dumps(api_body)
    URL = fr'https://api.twitter.com/2/oauth2/token?code={content}&grant_type=authorization_code&client_id=aXpOOWZkSm1JVHJ3S0o3YkJhSmI6MTpjaQ&redirect_uri=https://twitterfactchecker.herokuapp.com/callback&code_verifier=challenge'
    r = requests.post(url=URL, data=payload, headers=header)
    print(r.text)
    return HttpResponse('data recieve')
