#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value
title=form["title"].value
description=form["description"].value

opened_file=open('databox/'+title,'w')
opened_file.write(description)
opened_file.close()
os.rename('databox/'+pageId, 'databox/'+title)

print("Location: index.py?id="+title)
print()
