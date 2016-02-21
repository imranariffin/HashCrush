import os
from bottle import *
import facebook

global accessToken

@route('/')
def index(section='home'):
    return template('index')

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

@get('/sendAccessToken')
def get_access_token():
	print request.GET['accessToken']
	accessToken = request.GET['accessToken']
	
	graph = facebook.GraphAPI(accessToken)	
	profile = graph.get_object("me", fields=['context'])
	friends = graph.get_connections("me", "friends")

	return profile
	# return friends

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1337))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)
