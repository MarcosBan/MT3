#!/bin/bash

case $1 in 
	bind9) $(systemctl $2 $1) ;;
	nagios) $(systemctl $2 $1) ;;
	firewall) $(bash -c protege.sh $2) ;;
	*) exit 1 ;;
esac
