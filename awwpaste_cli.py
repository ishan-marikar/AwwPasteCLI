#!/usr/bin/env python

import requests
import sys
import urllib

url = "http://awwpaste.local/api/"


def Paste( textToPaste ):
	payload = {'text': textToPaste}
	data =  requests.post(url, params = payload);
	response = data.json()
	return response
	
def Main():
	keys = Paste(sys.stdin.read())
	print "Your AwwPaste link is %s" % keys['pasteID']
	print "Your AwwPaste delete link is %s" % keys['deleteKey']
	exit()

if __name__ == '__main__':
	Main()
	
	
