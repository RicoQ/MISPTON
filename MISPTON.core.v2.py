#!bin/python
#-*- coding:utf8 -*-
from scapy.all import *
import ISPRoute as ISP
#import Color as C

def Setup():
   os.system('clear')
   print "\n\nStarting MISPTON\n\n"

def Stop():
   print "\n\nUser stopped MISPTON\n\n"
   pass

def Run(pkt,T):
   try:
      if (str(pkt[IP].dst) == str(' <Remote VPN Server IP> ')) and (str(pkt[TCP].dport) == str(' <VPN Port> ')):
  #IE if (str(pkt[IP].dst) == str('8.8.8.8')) and (str(pkt[TCP].dport) == str('443')):
         print "\n----------------------------"
         ISP.ToISP(pkt,T)
      else: pass
   except: pass
	
if __name__ == '__main__':

  Setup()
  try:
     print "\nstarting routing through all ISP\n"
     while True:
	for T in range(1,10):
	    pkt=sniff(count=1)[0]
	    Run(pkt,T)
  except KeyboardInterrupt:
        Stop()	
