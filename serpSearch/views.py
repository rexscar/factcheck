from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
import requests
import json

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')

def normalSearch(request,*args,**kwargs):
    newchanels={'Bloomberg.com',"BBC","Daily Mail","Fox News"}
    print(request.body)
    parm=request.GET
    print("query: ",parm['query'])
    data=callgoogleSerp(parm['query'])
    print(type(data))
    # dictdata=json.loads(data)
    # print(type(dictdata))
    print(data["news_results"])

    return JsonResponse({'data':data["news_results"]})

def callgoogleSerp(query):
    endpoint=fr"https://serpapi.com/search.json?q={query}&tbm=nws&api_key=08a61966793f1c47beb6e5fcbabc1ac8cee2da74d468a4f51d8e5712e674ad52"

    getResponse=requests.get(endpoint)
    data=getResponse.json()
    # print(type(getResponse.text))
    return data