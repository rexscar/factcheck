from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
import requests

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')

def normalSearch(request,*args,**kwargs):
    print(request.body)
    parm=request.GET
    print("query: ",parm['query'])
    data=callgoogleSerp(parm['query'])
    # print(dir(request))
    return JsonResponse(data)

def callgoogleSerp(query):
    endpoint=fr"https://serpapi.com/search?q={query}"
    getResponse=requests.get(endpoint)
    print(type(getResponse.text))
    return getResponse.json()