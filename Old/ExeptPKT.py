#!bin/python
#-*- coding:utf8 -*-
from scapy.all import *
from Scan import *
import os, sys


def Run(pkt, Hosts, ifname):
    ifname=Ethernet(pkt, Hosts, ifname)
    return ifname

def Ethernet(pkt, Hosts, ifname):
   try:
      if (hex(pkt[Ether].type) == hex(0x0800)) or (hex(pkt[Ether].type) == hex(0x86dd)): ifname=Protocol(pkt, Hosts, ifname)  
   except:
      ifname = "Toto" 
   return ifname

def Protocol(pkt, Hosts, ifname):
    #print "Hosts = "+str(Hosts)
   try: 
      if (str(pkt[Ether].dst)) in Hosts.keys :
         print str(pkt[TCP].sport) + str(pkt[TCP].dport) 
         if (str(pkt[TCP].sport) == str(45022)) or (str(pkt[TCP].dport) == str(45022)): ifname="Pass"
         else: ifname = "Tata" 
      elif (str(pkt[TCP].sport) == str(45022)) or (str(pkt[TCP].dport) == str(45022)): ifname="Pass"
      elif (hex(pkt[IP].proto) == hex(0x06)) or (hex(pkt[IP].proto) == hex(0x11)): ifname="Null"
      else: ifname="Titi"
   except:
      ifname = "error"   
   return ifname
