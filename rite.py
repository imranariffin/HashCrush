# Use RiteTag API (http://ritetag.com/rest-api) to get list of similar hashtags & their viral potential.
# API Doc: http://docs.ritetag.apiary.io/

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
hashtags = ["toyota" ]

def lulz():
    ret = []
    for i in hashtags:
        url = "https://ritetag.com/api/v2/historical-data/"+i
        auth = OAuth1Session(client_key = ck, client_secret =  cs, resource_owner_key = ot,resource_owner_secret = os)
        r = auth.get(url).json()["data"]
        headers = ["date", "density", "mentions", "retweets", "unique", "color"]
        # wr.writerow(headers)
        for oneDayStat in r:
            row = []
            for temp in range(0,len(headers)):
                row = row + [oneDayStat[headers[temp]]]
            print row
            ret.append(row)
    return ret
    print ("Done")


if __name__=="__main__":
    lulz()

#print "data:\n"+json.dumps(r.json(), indent=4, sort_keys=True)
#0: white (underused)
#1: red (overused)
#3: green (hot now)
#2: blue (long life)
