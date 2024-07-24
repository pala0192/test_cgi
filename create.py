#!C:\Python38\python.exe
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os

file= os.listdir('databox')

listStr = ''
for item in file:
    listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)

form = cgi.FieldStorage()
if  'id' in form:
    pageId = form["id"].value
    description = open('databox/'+pageId, 'r').read()
else : 
    pageId = 'Welcome'
    description = 'Hello, web'

print('''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Practice</title>
    </head>
<body>
    <h1><a href="index.py">Web</a></h1>
    <ol>{listStr}
    </ol>
    <a href="create.py">create</a>
    
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title">
        </p>
        <p><textarea rows="10" name="description"
        placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
    '''.format(title=pageId, desc= description, listStr=listStr))