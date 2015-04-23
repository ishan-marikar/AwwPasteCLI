#!/usr/bin/env python

import requests
import json
import sys
import urllib

url = "http://localhost:63342/AwwPasteV2/api/"


def Paste( textToPaste ):
	payload = {'text': textToPaste}
	data =  requests.post(url, params = payload);
	binary = data.content
	response = json.loads(binary)
	return response
	
def Main():
	#total = ""
	#for line in sys.stdin:
	#	total += line
	keys = Paste(sys.stdin.read())
	print "Your AwwPaste link is %s" % keys['pasteID']
	print "Your AwwPaste delete link is %s" % keys['deleteKey']
	exit()

if __name__ == '__main__':
	Main()
	
	
