#!/usr/bin/env python
"""Minimal Twitter client

Command line application in docopt

Usage:
    tw_docopt.py [options] (timeline | mentions | retweets)
    tw_docopt.py -h | --help
    tw_docopt.py --version

Options:
    -h --helpShow this screen.
    --versionShow version.
    --api-key KEYTwitter API key.
    --api-secret SECRETTwitter client access token
    --access-secret SECRETTwitter client access secret 

"""

import os 

from docopt import docopt

import twitterlib

#Maps command line flags to environment variables.
ENV_VARS = {
	'--api-key': 'eAuQoYw9ffXtY5LdZm4Gmksfx',
	'--api-secret' : '5KiTpWGbTG8dtRaBuhcLdoT1jp12vRnr3pJ4yAUDXKLUkoMVk8',
	'--access-token' : '	360352221-e2oxvLe97TNGQZuM2vdCEy8zBx2JBGItPClOxsFv',
	'--access-secret' : '	hUjCvYHdPLppWeRfidaf0Yfo4Xbu61uZ8ze64rtqnVNC1'


}

#Sub-commands for select Twitter feeds.
def timeline(api):
	"Displays recent tweets from users timeline"
	for status in api.timeline:
		print u"%s: %s" % (status.user.screen_name, status.text)
 
def mentions(api):
	"Displays recent tweets mentioning user"
	for status in api.mentions:
		print u"%s: %S" % (status.user.screen_name, status.text)

def retweets(api):
	" Displays recent tweet for user's timeline"
	for status in api.retweets:
		print u"%s: %s" % (staus.user.screen_name, status.text)

SUB_COMMANDS = {
	'timeline': timeline,
	'mentions': mentions,
	'retweets': retweets

}		

# Command line execution.
if __name__ == '__main__':
	arguments = docopt(__doc__, version="1.0.0")

	#update missing auth tokens from environment variables.
	for optiion in arguments:
		if option not in EVR_VARS:
			continue
		if arguments[option] is not None:
			continue
		arguments[option] = os.environ[ENV_VARS[option]]

    #Create Twitter API object.
	api = twitterlib.API(
	 	arguments['--api-key'],
	 	arguments['--api-secret'],   
    	arguments['--access-token'],
    	arguments['--access-secret']
    )

    # Run chosen sub-command.
   	for command in SUB_COMMANDS:
   		if not arguments[command]:
   			continue
   		SUB_COMMANDS[command](api)
    	
    		
    
    		


			
