#!/usr/bin/python
import urllib2
import urllib
import re
from cookielib import CookieJar

#response = urllib.urlopen('http://s30000-102007-5ov.sipontum.hack.me/number.php') #change url when use hackme.
#req = response.read()

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
response = opener.open("http://s30000-102007-5ov.sipontum.hack.me/number.php")
req = response.read()

def getvalues(x):
	text = re.search('(\-\d+|\d+), (\-\d+|\d+)\S+\s+\S+\s(\w+)',x)
	result = text.group(1,2)
	return result

print getvalues(req)

def getcondition(x):
	text = re.search('(maximum|minimum)',x)
	result = text.group(1)
	return result

print getcondition(req)

def calculate(x,y):
	if y == 'maximum':
		x=max(x)
	else :
		x=min(x)
	return x

print calculate(getvalues(req),getcondition(req))

formdata = { "number" : calculate(getvalues(req),getcondition(req)), "submit": "submit"}
response = opener.open("http://s30000-102007-5ov.sipontum.hack.me/proc.php")
req = response.read()

print req
