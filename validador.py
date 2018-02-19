#!/usr/bin/python
#-*- coding: utf8 -*-
import re
#var = raw_input("RG: ")
#if re.match("^[0-9]{1,3}(\.?[0-9]{3}){2}-?[0-9a-zA-z]$", var):
#	print("Valido!")
#else:
#	print("Invalido!")


var = raw_input("E-mail: ")
if re.match("^[a-z]+([.-_][0-9a-z]|[0-9])*@[a-z]+([.-_][0-9a-z]|[0-9])*(\.com|\.br|\.com\.br)", var):
	print("Valido!")
else:
	print("Invalido!")
