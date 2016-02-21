import os
from bottle import *
import json
from pymongo import MongoClient
import datetime
from twitter_config import *

client = MongoClient()
db = client.db
db_related_tweets = db.db_related_tweets


global accessToken

# import 


import twitter as t
twitter = t.Api(
	consumer_key=consumer_key, 
	consumer_secret=consumer_secret, 
	access_token_key=access_token_key,
	access_token_secret=access_token_secret)

@route('/')
def index(section='home'):
	# print twitter.VerifyCredentials()
	return template('index')

@route('/tweets')
def tweets():
	tweets = twitter.GetSearch(term=' !!happybirthday')
	ret = []
	for tweet in tweets:
		print tweet
		ret.append(str(tweet))
	# return 'bernt'
	response.content_type='application/json'
	return json.dumps(ret)

@get('/hashcrush')
def __suggest():
	return template('hashcrush')

def get_related_tweets(tweet_key_words):
	related_tweets = []
	for key_word in tweet_key_words:
		tweets = db_related_tweets.find_one({'key_word' : key_word})
		if tweets==None:
			print "None"
			tweets = twitter.GetSearch(term=key_word, count=100)
			db_related_tweets.insert({'key_word' : key_word, 'tweets' : map(lambda tw: tw.text, tweets), 'date' : datetime.datetime.utcnow()})
		elif (datetime.datetime.utcnow() - tweets['date']).seconds > 600:
			print "more than 10 minutes"
			db_related_tweets.delete_one({'key_word' : key_word})
			tweets = twitter.GetSearch(term=key_word, count=100)
			db_related_tweets.insert({'key_word' : key_word, 'tweets' : map(lambda tw: tw.text, tweets), 'date' : datetime.datetime.utcnow()})
		else:
			print "oredy in db"
			tweets = tweets['tweets']
		related_tweets.extend(tweets)
	return related_tweets

def jsonify_tweets(tweets):
	return json.dumps(map(lambda e: str(e), tweets))

def find_hashtags(tweet_text):
	hashtags = []
	for word in tweet_text.split(" "):
		i = word.find('#')
		if word.find('#') != -1:
			hashtag = word[word.find('#'):]
			hashtags.append(hashtag.lower())
	return hashtags

def hashtag_count(tweet_key_words):
	hashtag_count = dict()
	related_tweets = get_related_tweets(tweet_key_words)
	# related_tweets.extend(get_related_tweets(tweet_key_words))

	for tweet in related_tweets:
		ret = tweet
		for hashtag in find_hashtags(tweet):
			ret += " : " + hashtag
			if hashtag not in hashtag_count.keys():
				hashtag_count[hashtag] = 1
			else:
				hashtag_count[hashtag] += 1
		# print ret
	return hashtag_count

def suggest(tweet_key_words):
	import operator
	h_count = hashtag_count(tweet_key_words)
	print h_count

	ret = map(lambda e:{e[0] : e[1]}, sorted(h_count.items(), key=operator.itemgetter(1), reverse=True))
	return ret[:10]

@post('/get-hashcrush')
def get_hashcrush():
	key_words = request.POST.get('tweet').split(" ")
	related_tweets = get_related_tweets(key_words)
	# print hashtag_count(key_words)
	return json.dumps(suggest(key_words))

@error(404)
def error404(error):
    return 'This is not the page you are looking for.'

@get('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='static')
    
@get('/bower_components/<filepath:path>')
def bower_files(filepath):
    return static_file(filepath, root='bower_components')

@get('/get-friends')
def get_friends():
	return "calls facebook API and returns list of friends in JSON"

@get('/fb-try')
def fb_try():
	return template('fb-test')

@post('/hashcrushtable')
def printout1():
	key_words = request.POST.get('tweet').split(" ")
        related_tweets = get_related_tweets(key_words)
        print hashtag_count(key_words)
        # return jsonify_tweets(related_tweets)
	basket=suggest(key_words)
	return template('hashcrushtable', basket=basket)

@get('/hashcrushtable')
def lul():
	return template('hashcrushtable', basket=[])


# @get('/sendAccessToken')
# def get_access_token():
# 	print request.GET['accessToken']
# 	accessToken = request.GET['accessToken']
	
# 	# graph = facebook.GraphAPI(accessToken)	
# 	graph = GraphAPI(accessToken)
# 	# profile = graph.get_object("me", fields=['posts', 'context'])
# 	# friends = graph.get_connections("me", "friends")

# 	return graph.get('me/posts', retry=10)
# 	# return graph.get('me/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1337))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)


