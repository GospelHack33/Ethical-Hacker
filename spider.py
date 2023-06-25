import requests
import sys
import os
from colorama import Fore
import time

os.system('clear')

blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
yellow = Fore.YELLOW

if len(sys.argv) == 2:
   pass
else:
   print(yellow+'\n [+] Usage - python spider.py <url>\n'+white)
   exit(0)

try:
    requests.get(str(sys.argv[1]))
except requests.exceptions.MissingSchema:
    print(red+'\n [+] Invalid URL\n'+white)

print(yellow+'*'*50)
print(green+f'\n [+] Spider Attack Started... \n [+] URL: {str(sys.argv[1])}\n')
print(yellow+'*'*50)
time.sleep(2)
print()
print(yellow+'*'*50)
print(yellow+'\n [+] Scanning For Directories...\n'+white)
print(yellow+'*'*50)
dirs = open('dir.txt', 'r')
line = 0
for dir in dirs.read().split('\n'):
    try:
        result = requests.get(str(sys.argv[1]+dir+'/')).status_code
        time.sleep(2)
        if result == 200:
           print(red+f'\n{line}. Found Directory - {dir}\n')
           line+=1
    except requests.exceptions.InvalidURL:
        print(blue+'\n [+] Add / At The End Of The URL\n'+white)
        break

