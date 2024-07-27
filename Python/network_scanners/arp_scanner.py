from scapy.all import ARP, Ether, srp
import ipaddress
import socket

def arp_scan(subnet):
    # Create an ARP request for the given subnet
    arp = ARP(pdst=str(subnet))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and capture the response
    result = srp(packet, timeout=2, verbose=0)[0]

    # Extract and print the IP and MAC addresses of the discovered devices
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def resolve_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = None
    return hostname

def main():
    subnet = ipaddress.ip_network('192.168.0.0/24', strict=False)
    print(f"Scanning subnet: {subnet}")
    devices = arp_scan(subnet)
    for device in devices:
        hostname = resolve_hostname(device['ip'])
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {hostname if hostname else 'N/A'}")

if __name__ == "__main__":
    main()
