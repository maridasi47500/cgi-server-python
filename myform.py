#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hi there ! </p>"
print "<p>Whats up </p>"
print "<p>go to <a href=\"/mypage.py\">My page</a></p>"
arguments = cgi.FieldStorage()
for i in arguments.keys():
 print "<p>"+str(i)+" : "+str(arguments[i].value)+"</p>"
