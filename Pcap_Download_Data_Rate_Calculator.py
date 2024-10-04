import sys
import pyshark
from datetime import timedelta

def main():

    fname = sys.argv[1]

    cap = pyshark.FileCapture(fname)

    count = 0
    total_size = 0

    for packet in cap:
        packet_size = int(packet.length)
        total_size += packet_size
        count+=1

    total_size_mb = total_size/1000000

    first_packet = cap[0]
    last_packet = cap[count-1]

    first_packet_time = first_packet.sniff_time
    last_packet_time = last_packet.sniff_time
    delta = last_packet_time - first_packet_time

    total_time = float(timedelta.total_seconds(delta))
    
    print("Download data rate is:",total_size_mb/total_time, "Mbps")

if __name__ == "__main__":
    main()
