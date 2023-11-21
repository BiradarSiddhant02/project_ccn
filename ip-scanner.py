from scapy.all import ICMP, IP, sr1
from multiprocessing import Pool

def send_icmp_request(ip):
    packet = IP(dst=ip) / ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    
    if response and response.haslayer(ICMP):
        if response[ICMP].type == 0:  # Echo Reply
            print(f"IP Address {ip} is reachable.")
        elif response[ICMP].type == 3:  # Destination Unreachable
            print(f"IP Address {ip} is unreachable.")
    else:
        print(f"No response from {ip}")

def scan_local_network(ip_range):
    base_ip = '192.168.0.'
    start, end = ip_range

    for i in range(start, end):
        ip = base_ip + str(i)
        send_icmp_request(ip)

def split_ip_range(num_processes, total_ips):
    chunk_size = total_ips // num_processes
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], total_ips)  # Adjust the last range to cover remaining IPs
    return ranges

if __name__ == "__main__":
    num_processes = 32
    total_ips = 256

    ranges = split_ip_range(num_processes, total_ips)

    with Pool(num_processes) as pool:
        pool.map(scan_local_network, ranges)
