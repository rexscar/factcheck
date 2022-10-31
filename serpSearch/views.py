from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
import requests
import json
from serpSearch.models import Searches
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


bearer_token = os.getenv("BEARER_TOKEN")


def create_url(idin):
    tweet_fields = "tweet.fields=lang,author_id"
   
    ids = fr"ids={idin}"
 
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()
    

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')

#serch for query
def normalSearch(request,*args,**kwargs):
    newchanels={'Bloomberg.com',"BBC","Daily Mail","Fox News"}
    print(request.body)
    parm=request.GET
    print("onCall: ",parm)
    CheckUser,Tweetlink=parm["CheckUser"],parm["TweetLink"]
    Tweet_link_list=Tweetlink.split("/")
    print(Tweet_link_list)
    TwitterHandle=Tweet_link_list[3]
    TweetId=Tweet_link_list[-1].split("?")[0]
    # print(TweetId ,TwitterHandle)
    
    url = create_url(TweetId)
    json_response = connect_to_endpoint(url)
    print(json_response)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    print(json_response["data"][0]["text"])
    data=callgoogleSerp(json_response["data"][0]["text"])
    # print(type(data))
    # dictdata=json.loads(data)
    # print(type(dictdata))
    # print(data["news_results"])

    return JsonResponse({'data':data["news_results"]})

#call serpsearch api
def callgoogleSerp(query):
    endpoint=fr"https://serpapi.com/search.json?q={query}&tbm=nws&api_key=08a61966793f1c47beb6e5fcbabc1ac8cee2da74d468a4f51d8e5712e674ad52"

    getResponse=requests.get(endpoint)
    data=getResponse.json()
    # print(type(getResponse.text))
    return data



