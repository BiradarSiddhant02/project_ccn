from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())
    
def main():
#    sniff(iface = 'eno1', prn=packet_callback, filter='tcp')
     sniff(iface = 'wlo1', prn=packet_callback, filter='tcp')
    
if __name__ == '__main__':
    main()

