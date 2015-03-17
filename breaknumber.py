import urllib
import re

response = urllib.urlopen('http://s30000-102007-m3r.sipontum.hack.me/number.php') #change url when use hackme.
req = response.read()

def getvalues(x):
	line = str(x)
	text = re.search('(\-\d+|\d+), (\-\d+|\d+)\S+\s+\S+\s(\w+)',x)
	result = text.group(1,2,3)
	return result

print getvalues(req)

def calculate(result):
	if result[2] == 'maximum':
		x=max(result)
	else :
		x=min(result)
	return x

print calculate(getvalues(req))
