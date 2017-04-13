#!bin/python
#-*- coding:utf8 -*-
from scapy.all import *
import ISPRoute as ISP
import ExeptPKT as PKT  
import os, sys, Scan


def Setup(ifname):
  print "Starting MISPTON"
  ifname=Scan.NetScan(ifname)
  #print "ifname= "+str(ifname)
  return ifname 
  
def Sniffer():
  pkt=sniff(count=1)[0]
  return pkt

def Stop():
  print "User stopped MISPTON"

def Run(pkt,Hosts):
  ifname = "0"
  Check = PKT.Run(pkt, Hosts, ifname)
  print "Check = "+str(Check)
  if Check == "Null":
      for T in range(0,4): 
         if T == 1:
	    print "pkt N°1 = "+pkt.summary()
	    ISP.Route1(pkt)
	 if T == 2:
	    print "pkt N°2 = "+pkt.summary()
	    ISP.Route2(pkt)
	 if T == 3:
            print "pkt N°3 = "+pkt.summary()
	    ISP.Route3(pkt)
  elif Check == "ok": ISP.Normal(pkt)
  elif Check == "pass": pass
  elif Check == "toto": print "not IP trafic"    
  else:
	print "unknown"
	pass    	 
if __name__ == '__main__':
  A=[]
  Hosts=Setup(A)
  #print Hosts
  pkt=Sniffer()
  try:
     print "starting routing through all ISP"
     while True:
        Run(pkt,Hosts)
  except KeyboardInterrupt:
        Stop()	
