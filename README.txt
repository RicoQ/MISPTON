# MISPTON
Multy Internet Service Providers to One Network

-------------------------------------------------------

 Multi Internet Service Providers to One Network
    Version 0.1 (Alpha) by RicoQ
    Python  2.7.9 (Rasbian)
    Writen Specificaly for Raspberry PI-2 B
    
--------------------------------------------------------

 MISPTON is for those who have multiple ADSL connection 
   and would'd like to merge them into One network
	         _______
 LAN	        |       |
<---|	     ___|  ISP  |___                 
    |	    |   |_______|   |                  ______
 ___|___    |    _______    |     ______      |      |
|	|VPN|   |       |   | VPN|      |WAN /        \
|  RPI	|---|---|  ISP  |---|----| Sev  |---| Internet |
|_______|   |   |_______|   |    |______|    \        /
 	    |    _______    |                 |______|
 	    |___|       |___|
	        |  ISP  |
 	        |_______|

 This can have more than one Usage, but the purpose for
    me is to increase the Bandwith (by ISP connections).
 
--------------------------------------------------------
 
 For this to be effitiant, you need a Distant Server,
   and install a VPN server on it (I use OpenVPN), then
   the Raspberry PI has to be The Router (for your LAN),
   and a VPN client to the server distant. This is
   so that all Ethernet traffic passes throught the 
   Raspberry PI, in turn, this makes the ISPs become 
   "WAN Routers" on the way to Internet, so the traffic
   goes through one or the other, depending on the traffic
   of each (In theory ^^). The program (MISPTON) that 
   I'm trying to write is suppose to help the traffic in
   being sent through ALL IPSs.

   Exemple: You're streaming a video, the 1st Ethernet 
   packet is routed throught ISP_1, the 2sd Ethernet
   packet is routed throught ISP_2, and the 3rd through
   ISP_3, and back to the 1st, then 2sd, then 3rd again...
   so on and so on. (This multiplies your bandwith by the 
   number of connection ISP.]     
    
    
---------------------------------------------------------

Being relativly new to programming, as well as 100% self taught! My work might be a little basic and some times redondante.
If you decide to help explain any changes you make; why the changes? and how is it better?... so I might learn from my 
mistakes, thanx. (ps: please explain in ways a baby could understand... Comments such as "this or that already existe!!!" does
not help!, and I don't actually care, I'm not re-inventing the wheel, I'm learning by doing something I like and need 
for myself... it is much better (to my opinion) than doing some kind of "hello world" programing!)
