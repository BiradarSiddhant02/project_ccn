from scapy.all import ICMP, IP, sr1

def send_icmp_request(ip):
    packet = IP(dst=ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    
    if response and response.haslayer(ICMP):
        if response[ICMP].type == 0:  # Echo Reply
            print(f"IP Address {ip} is reachable.")
        elif response[ICMP].type == 3:  # Destination Unreachable
            print(f"IP Address {ip} is unreachable.")
    else:
        print(f"No response from {ip}")

def scan_local_network():
    base_ip = '192.168.0.'
    
    for i in range(1, 256):
        ip = base_ip + str(i)
        send_icmp_request(ip)

if __name__ == "__main__":
    scan_local_network()
