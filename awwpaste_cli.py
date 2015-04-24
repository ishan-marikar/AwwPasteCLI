#!/usr/bin/env python

import requests
import sys
import urllib

url = "http://awwpaste.local/"
apiUrl = url + "api/"


def Paste( textToPaste ):
	payload = {'text': textToPaste}
	data =  requests.post(apiUrl, params = payload);
	response = data.json()
	return response
	
def Main():
	input =  sys.stdin.read()
	print input
	keys = Paste(input)
	print "-" * 82
	print "Your AwwPaste link is %s?id=%s" % ( url , keys['pasteID'] )
	print "Your AwwPaste delete link is %s?id=%s&delete_key=%s" % ( url , keys['pasteID'], keys['deleteKey'] )
	exit()

if __name__ == '__main__':
	Main()
	
	
