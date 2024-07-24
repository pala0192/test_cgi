#!C:\Python38\python.exe
import cgi
form = cgi.FieldStorage()
title=form["title"].value
description=form["description"].value

opened_file=open('databox/'+title,'w')
opened_file.write(description)
opened_file.close()


print("Location: index.py?id="+title)
print()
