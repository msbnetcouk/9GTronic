# 9GTronic - Automating GNS3 virtual router labs

ql@schumacher:/gns3labs$ d

./  ../  ibgp-final-configs.zip
ql@schumacher:/gns3labs$



ql@schumacher:/gns3labs$ unzip ibgp-final-configs.zip -d .

Archive:  ibgp-final-configs.zip
  inflating: ./IBGP Internal BGP/Blossom.cfg  
  inflating: ./IBGP Internal BGP/Rose.cfg  
  inflating: ./IBGP Internal BGP/Lily.cfg  
  inflating: ./IBGP Internal BGP/Tulip.cfg  



ql@schumacher:~$ python 9GTronic.py

USAGE: python 9GTronic.py <project name> <project path>

Example:  python 9GTronic.py iBGP /gns3labs/IBGP\ Internal\ BGP/

ql@schumacher:~$ python 9GTronic.py iBGP /gns3labs/IBGP\ Internal\ BGP/

GNS Server: 2.2.12

Created new project 0f82a2ef-6db8-42d0-adf2-39abaede1419

Started node 368dd21a-faaf-4ce5-a421-08b285e97c13
Started node b27e56ec-bf5b-4f6d-aea9-263f8bf8bbdc
Started node 545afc76-fd04-4b21-a2e0-5a2977b8f529
Started node 4a65d7dc-0a31-46ff-858c-11e528b88a18

Linked 368dd21a-faaf-4ce5-a421-08b285e97c13 to 545afc76-fd04-4b21-a2e0-5a2977b8f529
Linked 368dd21a-faaf-4ce5-a421-08b285e97c13 to b27e56ec-bf5b-4f6d-aea9-263f8bf8bbdc
Linked 545afc76-fd04-4b21-a2e0-5a2977b8f529 to 4a65d7dc-0a31-46ff-858c-11e528b88a18
Linked b27e56ec-bf5b-4f6d-aea9-263f8bf8bbdc to 4a65d7dc-0a31-46ff-858c-11e528b88a18

Lab is now running in GNS3: http://127.0.0.1:3080/static/web-ui/server/1/project/0f82a2ef-6db8-42d0-adf2-39abaede1419



ql@schumacher:~$ python 9GTronic.py iBGP /gns3labs/IBGP\ Internal\ BGP/

GNS Server: 2.2.12

Project (http://127.0.0.1:3080/static/web-ui/server/1/project/0f82a2ef-6db8-42d0-adf2-39abaede1419) already exists. DELETE? [Y/n] 
Deleting... 0f82a2ef-6db8-42d0-adf2-39abaede1419

Created new project 4132fc79-3700-4d43-8f77-0c13e05f8c05

Started node d5065e84-c7e0-4c08-b0c1-0a46f0c8d2c1
Started node cf77e62b-cb48-41b5-b44d-eb7667209aca
Started node 884b71f3-14f9-4ad1-92fb-596763ec6fb8
Started node f3a21adb-bb7f-485a-aa21-8aac5444918d

Linked d5065e84-c7e0-4c08-b0c1-0a46f0c8d2c1 to 884b71f3-14f9-4ad1-92fb-596763ec6fb8
Linked d5065e84-c7e0-4c08-b0c1-0a46f0c8d2c1 to cf77e62b-cb48-41b5-b44d-eb7667209aca
Linked 884b71f3-14f9-4ad1-92fb-596763ec6fb8 to f3a21adb-bb7f-485a-aa21-8aac5444918d
Linked cf77e62b-cb48-41b5-b44d-eb7667209aca to f3a21adb-bb7f-485a-aa21-8aac5444918d

Lab is now running in GNS3: http://127.0.0.1:3080/static/web-ui/server/1/project/4132fc79-3700-4d43-8f77-0c13e05f8c05

ql@schumacher:~$ 





Press RETURN to get started!


*Mar  1 00:00:02.427: %LINEPROTO-5-UPDOWN: Line protocol on Interface VoIP-Null0, changed state to up
*Mar  1 00:00:02.655: %LINEPROTO-5-UPDOWN: Line protocol on Interface IPv6-mpls, changed state to up
*Mar  1 00:00:02.891: %SYS-5-CONFIG_I: Configured from memory by console
*Mar  1 00:00:03.007: %SYS-5-RESTART: System restarted --
Cisco IOS Software, 3600 Software (C3640-A3JS-M), Version 12.4(25d), RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Wed 18-Aug-10 06:58 by prod_rel_team
*Mar  1 00:00:03.019: %SNMP-5-COLDSTART: SNMP agent on host Tulip is undergoing a cold start
*Mar  1 00:00:03.047: %LINK-3-UPDOWN: Interface FastEthernet0/0, changed state to up
*Mar  1 00:00:03.051: %LINK-3-UPDOWN: Interface FastEthernet1/0, changed state to up
*Mar  1 00:00:03.055: %LINK-5-CHANGED: Interface FastEthernet2/0, changed state to administratively down
*Mar  1 00:00:03.055: %LINK-5-CHANGED: Interface FastEthernet3/0, changed state to administratively down
*Mar  1 00:00:03.707: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up
*Mar  1 00:00:03.767: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback1, changed state to up
*Mar  1 00:00:04.047: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up
*Mar  1 00:00:04.047: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet1/0, changed state to up
*Mar  1 00:00:04.055: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet2/0, changed state to down
*Mar  1 00:00:04.055: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet3/0, changed state to down
*Mar  1 00:00:43.283: %OSPF-5-ADJCHG: Process 1, Nbr 33.33.33.33 on FastEthernet1/0 from LOADING to FULL, Loading Done
*Mar  1 00:00:43.639: %OSPF-5-ADJCHG: Process 1, Nbr 22.22.22.22 on FastEthernet0/0 from LOADING to FULL, Loading Done
*Mar  1 00:01:06.979: %BGP-5-ADJCHANGE: neighbor 4.4.4.4 Up 
*Mar  1 00:01:08.447: %BGP-5-ADJCHANGE: neighbor 3.3.3.3 Up 
*Mar  1 00:01:09.767: %BGP-5-ADJCHANGE: neighbor 2.2.2.2 Up 
Tulip>

