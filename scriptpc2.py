from subprocess import call
import sys
import os
import re

variable= os.environ.get('GROUP_NUMBER')
text = '{% block title %}Simple Bookstore App{% endblock %}'

string1 = str(variable)

string= '{% block title %}'
string2= '{% endblock %}'
newstring= string + string1 + string2 





path=str(os.getcwd())
print(path)
path1= path +"/practica_creativa2/bookinfo/src/productpage"
path2=path +"/practica_creativa2/bookinfo/src/productpage/templates"
print(path)

call (["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
os.chdir(path1)
call (["python3", "-m", "pip", "install", "-r", "requirements.txt"])
os.chdir(path2)

d=open("index.html","r")
f=open("auxiliar.html","w")
for line in d:
    if "{% block title %}" in line:
        f.write(newstring)
    else:
        f.write(line)
f.close()
d.close()
call(["cp","auxiliar.html", "index.html"])
call(["rm", "auxiliar.html"])


d=open("productpage.html","r")
f=open("auxiliar.html","w")
for line in d:
    if "{% block title %}" in line:
        f.write(newstring)
    else:
        f.write(line)
f.close()
d.close()
call(["cp","auxiliar.html", "productpage.html"])
call(["rm", "auxiliar.html"])


os.chdir(path1)

d=open("productpage_monolith.py","r")
f=open("auxiliar.py","w")
for line in d:
    if "import asyncio" in line:
        f.write("import asyncio \n")
        f.write("import socket \n")
        f.write("hostname = socket.gethostname() \n")
        f.write("IPAddr = socket.gethostbyname(hostname)")
    else:
        f.write(line)
f.close()
d.close()
call(["cp","auxiliar.py", "productpage_monolith.py"])
call(["rm", "auxiliar.py"])


d=open("productpage_monolith.py","r")
f=open("auxiliar.py","w")
for line in d:
    if '"name": "http://{0}{1}:9080".format(detailsHostname, servicesDomain),' in line:
        f.write('"name": "http://{0}{1}:{2}".format(detailsHostname, servicesDomain,int(sys.argv[1])), \n')
    elif '"name": "http://{0}{1}:9080".format(ratingsHostname, servicesDomain),' in line:
        f.write('"name": "http://{0}{1}:{2}".format(ratingsHostname, servicesDomain,int(sys.argv[1])), \n')
    elif '"name": "http://{0}{1}:9080".format(reviewsHostname, servicesDomain),' in line:
        f.write('"name": "http://{0}{1}:{2}".format(reviewsHostname, servicesDomain,int(sys.argv[1])),\n')
    elif '"name": "http://{0}{1}:9080".format(detailsHostname, servicesDomain),' in line:
        f.write('"name": "http://{0}{1}:{2}".format(detailsHostname, servicesDomain,int(sys.argv[1])),\n')
    
    else:
        f.write(line)
f.close()
d.close()
call(["cp","auxiliar.py", "productpage_monolith.py"])
call(["rm", "auxiliar.py"]) 

d=open("productpage_monolith.py","r")
f=open("auxiliar.py","w")
for line in d:
    if " app.run(host='::', port=p, debug=True, threaded=True)" in line:
        f.write(" app.run(host="34.123.83.153", port=p, debug=True, threaded=True) \n")
    else:
        f.write(line)
f.close()
d.close()
call(["cp","auxiliar.py", "productpage_monolith.py"])
call(["rm", "auxiliar.py"])

call(["python3","productpage_monolith.py","{}".format(sys.argv[1])])




