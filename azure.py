# Use RiteTag API (http://ritetag.com/rest-api) to get list of similar hashtags & their viral potential.
# API Doc: http://docs.ritetag.apiary.io/

# This program fetches the predicted result using Azure. It returns an array of bool that indicates whether a given hashtag is predicted to be popular in the next few days, in the same order of the input array.

import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json
import requests
from requests_oauthlib import OAuth1Session
import json
import sys
import csv

# Get your tokens & keys @ http://ritetag.com/developer/signup
ck = "c0ef2f5154fc378f54394ef93178136a056c942d8"
cs = "e31014e75459ae271ba5b456db9a5699"
ot = "6275a82db921ef425965fda6f88468ee056c942d8"
os = "939bada22f32e4079893d390a6eb59b6"

# A list of trending hashtags
hashtags = []
headers = ["date", "density", "mentions", "retweets", "unique", "color"]
useBool = []

def getRiteTagData (i):
    url = "https://ritetag.com/api/v2/historical-data/"+i
    auth = OAuth1Session(client_key = ck, client_secret =  cs, resource_owner_key = ot,resource_owner_secret = os)
    r = auth.get(url).json()["data"]
    for oneDayStat in r:
        row = []
        for temp in range(0,len(headers)):
            row = row + [oneDayStat[headers[temp]]]
        if row[len(row)-1] == 2 or row[len(row)-1] == 3:
            row = row + [1]
        else:
            row = row + [0]
    print ("Twitter data for " + i + " has been fetched.")
    getPrediction (row)


#print "data:\n"+json.dumps(r.json(), indent=4, sort_keys=True)
#0: white (underused)
#1: red (overused)
#3: green (hot now)
#2: blue (long life)

def getPrediction(riteTagData):
    data =  {
        
        "Inputs": {
            
            "input1":
                {
                    "ColumnNames": ["date", "density", "mentions", "retweets", "unique", "color", "Use"],
                        "Values": [ riteTagData, ]
                    },        },
                "GlobalParameters": {
    }
    }

    body = str.encode(json.dumps(data))

    url = 'https://asiasoutheast.services.azureml.net/workspaces/ce4257780afa44f0bc0f392480b49650/services/461aa0d3c327446e9f10cfe458de3147/execute?api-version=2.0&details=false'
    api_key = 'fmvRT4I9cUskU/n9EiNgx6zcA14Ptgk1cbgVk7s3hjCIsvcD51eFgVUKXryb6Tx9+HaZjz/U9RyrIu7z7YHULQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)
        
        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)
        
        result = response.read()
        result = json.loads(result)
        #print(result)
        useBool.append( [result["Results"]["output1"]["value"]["Values"][0][4]])
    except urllib2.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))

#usage: start(listOfHashtags) -> array of bool in the same order
def start (listOfHashtags):
    hashtags = listOfHashtags
    print("List of #: ", hashtags)
    for i in hashtags:
        getRiteTagData(i)
    return useBool
