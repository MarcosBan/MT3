#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()

import os
menu=var.split("=")[0]
print("content-type: text/html")
print("")

if menu == "d_i":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh bind9 start")
	print "Start OK"
elif menu == "d_p":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh bind9 stop")
	print "Stop OK"
elif menu == "d_r":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh bind9 restart")
	print "Restart OK"
elif menu == "f_i":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh firewall start")
	print "Stop OK"
elif menu == "f_p":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh firewall stop")
	print "Restart OK"
elif menu == "f_r":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh firewall restart")
	print "Stop OK"
elif menu == "n_i":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh nagios start")
	print "Restart OK"
elif menu == "n_p":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh nagios stop")
	print "Stop OK"
elif menu == "n_r":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh nagios restart")
	print "Restart OK"
