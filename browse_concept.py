#!/usr/bin/env python


import socket
import struct
import time
import os,webbrowser




iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                        "Internet Explorer\\IEXPLORE.EXE")
browser = webbrowser.get(iexplore)


image_files = [
'C:/Users/Ethan/Pictures/testing/msi_logo.png',
'C:/Users/Ethan/Pictures/testing/Nvidia_logo.png',
'C:/Users/Ethan/Pictures/testing/python_logo.png',
'C:/Users/Ethan/Pictures/testing/windows.png'
]


MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
        #print(sock.recv(10240))
        for image in image_files:
                browser.open(image)
