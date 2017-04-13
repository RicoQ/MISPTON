#!/bin/python
#-*- coding:utf8 -*-
from scapy.all import *
import Color as C

def Route1(pkt):
   conf.route.add(host='163.172.26.106', gw='192.168.5.1')
   send(pkt)
   print "----------------------------\n"
   conf.route.resync()

def Route2(pkt):
   conf.route.add(host='163.172.26.106', gw='192.168.5.1')
   send(pkt)
   print "----------------------------\n"
   conf.route.resync()

def Route3(pkt):
   conf.route.add(host='163.172.26.106', gw='192.168.5.1')
   send(pkt)
   print "----------------------------\n"
   conf.route.resync()

def Normal(pkt):
   send(pkt)

def ToISP(pkt,T):
   print str(T) 
   if   (T == 1) or (T == 4) or (T == 7):
      print "Sending PKT Throught IPS N°1"
      print C.P+"pkt N°1 = "+C.C+pkt.summary()+C.W+" to Remote Server\n"
      Route1(pkt)
   elif (T == 2) or (T == 5) or (T == 8):
      print "Sending PKT Throught IPS N°2"
      print C.P+"pkt N°2 = "+C.C+pkt.summary()+C.W+" to Remote Server\n"
      Route2(pkt)
   elif (T == 3) or (T == 6) or (T == 9):
      print "Sending PKT Throught IPS N°3"
      print C.P+"pkt N°3 = "+C.C+pkt.summary()+C.W+" to Remote Server\n"
      Route3(pkt)    
