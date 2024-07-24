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
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action='''
      <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{0}">
        <input type="submit" value="delete">
      </form>
    '''.format(pageId)
else : 
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link=''
    delete_action=''


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
  {ud_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}
  </p>
</body>
</html>
      '''.format(title=pageId, desc= description, listStr=listStr, ud_link=update_link, delete_action=delete_action))

