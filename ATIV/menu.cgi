#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()

import os
menu=var.split("=")[0]
print("content-type: text/html")
print("")

if menu == "d_i":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh bind9 start")
	print "Start DNS OK"
elif menu == "d_p":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh bind9 stop")
	print "Stop DNS OK"
elif menu == "d_r":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh bind9 restart")
	print "Restart DNS OK"
elif menu == "f_i":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh firewall start")
	print "Start Firewall OK"
elif menu == "f_p":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh firewall stop")
	print "Stop Firewall OK"
elif menu == "f_r":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh firewall restart")
	print "Restart Firewall OK"
elif menu == "n_i":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh nagios3 start")
	print "Start Nagios OK"
elif menu == "n_p":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh nagios3 stop")
	print "Stop Nagios OK"
elif menu == "n_r":
	os.system("sudo /var/www/html/cgi-bin/site/services.sh nagios3 restart")
	print "Restart Nagios OK"
