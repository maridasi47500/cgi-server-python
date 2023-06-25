#!/usr/bin/env python
print """
<!DOCTYPE>
<html>
<head>
<title>my test</title>
</head>
<body>
<form name="f1" method="post" action="myform.py">
<table>
<tr><td>First Name </td><td><input type=text name=f_name><td></tr>
<tr><td>Second Name</td><td> <input type=text name=s_name></td></tr>
<tr><td>Sex</td><td> <input type=radio name=r1 value=male> Male 
<input type=radio name=r1 value=female> Female </td></tr>
<tr><td>Class</td><td> <select name=class>
<option value='Three'>Three</option>
<option value='Four'>Four</option>
<option value='Five'>Five</option>
</select>
 </td></tr>
 <tr><td><input type=submit value=Submit></td><td> </td></tr>
</table>
</form>
</body>
</html>
"""
