#!/usr/bin/python
import urllib2
import urllib
import re
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
rnd = 0

targeturl = 'http://s30000-102007-q0k.tarentum.hack.me/number.php'
submiturl = 'http://s30000-102007-q0k.tarentum.hack.me/proc.php'


while (rnd < 60):
	response = opener.open(targeturl)
	req = response.read()


	def getvalues(x):
		text = re.search('\<p\>(.*)\<br \/\>T',x)
		text1 = text.group(1)
		text2 = re.findall('(\-\d+|\d+)',text1)
		return text2

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
			x=max(map(int,x))
		else :
			x=min(map(int,x))
		return x

	print calculate(getvalues(req),getcondition(req))

	number = calculate(getvalues(req),getcondition(req))

	formdata = { "number" : number, "submit": "submit"}
	data_encoded = urllib.urlencode(formdata)
	response = opener.open(submiturl,data_encoded)
	req2 = response.read()

	score = getscore(req)
	print "Score : "+score

	rnd=rnd+1

	def getflag(flag):
		text = re.search('Congratulation\s\S+\s\S+\s(.*)\<\/center>',flag)
		flag = text.group(1)
		return flag

print "The Flag is : "+getflag(req)
