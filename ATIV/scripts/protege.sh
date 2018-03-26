!#/bin/bash
#Politica do FirewalL
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

#Limpar regras das chains
iptables -F

