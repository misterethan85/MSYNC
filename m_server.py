#!/usr/bin/env python


import socket
import struct
import time

def main():
  MCAST_GRP = '224.1.1.1'
  MCAST_PORT = 5007
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
  while True:
  	sock.sendto(b'SUCCESS', (MCAST_GRP, MCAST_PORT))
  	time.sleep(5)

if __name__ == '__main__':
  main()
