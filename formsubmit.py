#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
try:
    f_name=form["f_name"].value
except:
    f_name=' First name is blank '

try:
    s_name=form["s_name"].value
except:
    s_name=' Second name is blank '

try:
    r1=form["r1"].value
except:
    r1=' No selection of  Sex'

try:
    my_class=form["class"].value
except:
    my_class= ' Select Class '

print("any text")
#print("<br><b>First Name</b>"+f_name)
#print("<br><b>Second Name</b>"+s_name)
#print("<br><b>Sex</b>"+r1)
#print("<br><b>Class</b>"+my_class)
