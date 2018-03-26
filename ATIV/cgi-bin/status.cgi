#!/usr/bin/python
#-*- coding: utf8 -*-
import os
print("content-type: text/html")
print("")

print("<html>")
print("<body>")
print("<h1>Status</h1>")
print("<h2>")
os.system("sudo /var/www/html/cgi-bin/site/stats.sh")
print("</h2>")
print("</body>")
print("</html>")
