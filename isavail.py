import urllib2,cookielib
import sys
firstarg=sys.argv[1]
import re
def isavail(domain):
  check='http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=' + domain
  send = urllib2.Request(check)
  response = urllib2.urlopen(send).read()
  if re.compile("has already been registered by").search(response) is None:
    print "Yes"
  else:
    print "No"
isavail(firstarg)
