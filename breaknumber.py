#!/usr/bin/python
import urllib2
import urllib
import re
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
rnd = 0


while (rnd < 60):
	response = opener.open("http://s30000-102007-5ov.sipontum.hack.me/number.php")
	req = response.read()


	def getvalues(x):
		text = re.search('(\-\d+|\d+), (\-\d+|\d+)\S+\s+\S+\s(\w+)',x)
		result = text.group(1,2)
		return result

	print getvalues(req)

	def getscore(x):
		text = re.search('Score:\s(\d+)\<\/p',x)
		result = text.group(1)
		return result

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
	number = calculate(getvalues(req),getcondition(req))

	formdata = { "number" : number, "submit": "submit"}
	data_encoded = urllib.urlencode(formdata)
	response = opener.open("http://s30000-102007-5ov.sipontum.hack.me/proc.php",data_encoded)
	req2 = response.read()


	score = getscore(req)
	print "Score : "+score

	rnd=rnd+1
