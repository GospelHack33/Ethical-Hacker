# nmap (network mapper) framework for carrying various exploit on a specific target
# this tool is for educational purposes only, use wisely
# admin - gospel chukwunonso
import os
import subprocess
from cfonts import render
from colorama import Fore
import time

# clear screen
if os.name == 'posix':
   os.system('clear')

# app screen title output
print('*'*62)
print(render('MapSploit', colors=['yellow', 'red']))
print('*'*62)
print(Fore.YELLOW+'[*] Nmap Framework v5.0'+Fore.WHITE)
print(Fore.YELLOW+'\n[*] Created By - Gospel Chukwunonso'+Fore.WHITE)
# requires termux to run
if 'com.termux' in os.listdir('/sdcard/Android/data'):
   pass
else:
   print(Fore.YELLOW+'\n[*] Run This Framework In Termux Environment...'+Fore.WHITE)
   print(Fore.RED+'\n[*] Requires termux to run!!!\n'+Fore.WHITE)
   exit(0)
# install packages
print(Fore.BLUE+'\n[+] Checking for required package...'+Fore.WHITE)
time.sleep(3)

# check if package is installed
if 'nmap' in os.listdir('/data/data/com.termux/files/usr/bin/'):
   pass
else:
   print(Fore.RED+'\n[*] Package Not Found... Execute The Below Command To Install Missing Package'+Fore.WHITE)
   print(Fore.YELLOW+'[*] apt install nmap'+Fore.WHITE)
   exit(0)

# main
print(Fore.GREEN+'\n[*] Starting MapSploit Console...'+Fore.WHITE)
time.sleep(4)
print(Fore.YELLOW+'\nSuccess - [ MapSploit Successfully Installed ]'+Fore.WHITE)
while True:
      console = input(Fore.BLUE+'\n(MapSploit)\n||\n||===========> '+Fore.WHITE)
      if console == 'help':
         print(Fore.YELLOW+'\nhelp ------> mapsploit help'+Fore.WHITE)
         print(Fore.YELLOW+'\nlist script ------> list mapsploit exploits scripts'+Fore.WHITE)
         print(Fore.YELLOW+'\nhost <ip|host name> ------> set host to scan'+Fore.WHITE)
         print(Fore.YELLOW+'\ncheck host ------> check if host is set'+Fore.WHITE)
         print(Fore.YELLOW+'\nset script <script name> ------> set mapsploit script to scan on target'+Fore.WHITE)
         print(Fore.YELLOW+'\nrun ------> start scan'+Fore.WHITE)
         print(Fore.YELLOW+'\ncheck vuln ------> check if target is vulnerable'+Fore.WHITE)
         print(Fore.YELLOW+'\nexit ------> exit mapsploit'+Fore.WHITE)
         print(Fore.YELLOW+'\nupdate script ------> update mapsploit scripts'+Fore.WHITE)
         print(Fore.YELLOW+'\nscan port ------> scan for open port in target'+Fore.WHITE)
         print(Fore.YELLOW+'\nreset mapsploit ------> reset mapsploit to default'+Fore.WHITE)
         print(Fore.YELLOW+'\nexploit ssh <port> ------> exploit into the system (requires USER & PASS)'+Fore.WHITE)
         print(Fore.YELLOW+'\nclear ------> clear screen'+Fore.WHITE)
      elif console == 'list script':
           script = os.listdir('/data/data/com.termux/files/usr/share/nmap/scripts')
           line = 0
           for scr in script:
               print(Fore.YELLOW+f'\n [{line}] '+scr+Fore.WHITE)
               line += 1
      elif console[:5] == 'host ':
           print(Fore.YELLOW+f'\n[+] Host ------> {console[5:]}'+Fore.WHITE)
           if console[5:] == '':
              print(Fore.RED+'\n[*] Please specify a target '+Fore.WHITE)
           f = open('target.txt', 'w').write(console[5:])
      elif console == 'check host':
           print(Fore.RED+'\nTarget'+Fore.WHITE)
           host = open('target.txt', 'r').read()
           print(Fore.RED+f'\n------\n[-{host}-]'+Fore.WHITE)
      elif console == 'reset mapsploit':
           f = open('target.txt', 'w').write('')
           f = open('exploit.txt', 'w').write('')
           print(Fore.YELLOW+'\n[+] MapSploit Console Has Been Reset'+Fore.WHITE)
      elif console == 'clear':
           os.system('clear')
      elif console[:12] == 'exploit ssh ' or console[:11] == 'exploit ssh':
           tar = open('target.txt', 'r').read()
           if len(console[12:]) == 0:
              print(Fore.RED+'\n[+] Missing - Port Number...'+Fore.WHITE)
           else:
                if '.' not in tar:
                   print(Fore.RED+'\n[+] Host Not Set Or Maybe Invalid\n'+Fore.WHITE)
                else:
                   print(Fore.YELLOW+f'\n[+] Checking For SSH Session On {tar}'+Fore.WHITE) 
                   ssh_ses = subprocess.check_output(f'nmap -p {console[12:]} --open -sV {tar} -Pn', shell=True).decode()
                   if 'open' in ssh_ses and 'ssh' in ssh_ses:
                      print(Fore.RED+'\n[+] 200 -  SSH Session Started...'+Fore.WHITE)
                      username = input(Fore.BLUE+'\n[+] Username: '+Fore.WHITE)
                      print(Fore.YELLOW+f'\n[ Enter Password For {username}@{tar} ]\n'+Fore.WHITE)
                      login = subprocess.run(f'ssh {username}@{tar} -p {console[12:]}', shell=True)
                   else:
                      print(Fore.RED+f'\n[+] Connection Refuse... Host Is Down At Port {console[12:]}'+Fore.WHITE)
      elif console[:11] == 'set script ':
           scr_nme = console[11:]
           print(Fore.YELLOW+f'\n[+] Script ------> {scr_nme}'+Fore.WHITE)
           if '#' in scr_nme:
              print(Fore.RED+'\n[+] Error 507- script name has an ext, specify without an ext'+Fore.WHITE)
           else:
              script = os.listdir('/data/data/com.termux/files/usr/share/nmap/scripts')
              if scr_nme in script:
                 f = open('exploit.txt', 'w').write(scr_nme)
              else:
                 print(Fore.RED+f'\n[+] Error 400 - script {scr_nme} not found'+Fore.WHITE)

      elif console == 'check vuln':
            f = open('exploit.txt', 'r').read()
            target = open('target.txt', 'r').read()
            print(Fore.YELLOW+'\n[+] Vulnerability Scan Started...'+Fore.WHITE)
            vuln_scan = subprocess.check_output(f'nmap -sV --script=vulners {target} -Pn', shell=True).decode()
            print(Fore.YELLOW+f'\n[+] Vulnerability Scan Report For {target}\n'+Fore.WHITE)
            if 'vulners:' not in vuln_scan:
               print(Fore.RED+'\nVulnerability Status\n\n---------------------\nNOT VULNERABLE'+Fore.WHITE)
            else:
               print(Fore.RED+'\nVulnerability Status\n\n--------------------\nVULNERABLE'+Fore.WHITE)
      elif console == 'run':
           f = open('exploit.txt', 'r').read()
           if '.nse' not  in f:
              print(Fore.RED+'\n[+] Mapsploit Scan Script Not Set, Using Default MapSploit Scan...'+Fore.WHITE)
              tar = open('target.txt', 'r').read()
              if '.' not in tar:
                 print(Fore.RED+'\n[+] Error - Host Not Set Or Maybe Invalid'+Fore.WHITE)
              else:
                 print(Fore.YELLOW+'\n[+] MapSploit Scan Started...'+Fore.WHITE)
                 time.sleep(2)
                 print(Fore.RED+'\n[+] Using Default Script'+Fore.WHITE)
                 mps_scan = subprocess.check_output(f'nmap -sC {tar} -Pn', shell=True).decode()
                 print(Fore.YELLOW+'\n[+] MapSploit Scan Completed...\n'+Fore.WHITE)
                 print(Fore.RED+mps_scan+Fore.WHITE)
           else:
              tar = open('target.txt', 'r').read()
              if '.' not in tar:
                 print(Fore.RED+'\n[+] Error - Host Not Set Or Maybe Invalid'+Fore.WHITE)
              else:
                 print(Fore.YELLOW+'\n[+] MapSploit Scan Started...'+Fore.WHITE)
                 time.sleep(2)
                 print(Fore.RED+f'\n[+] Using Script {f}'+Fore.WHITE)
                 if 'brute' in f:
                    print(Fore.YELLOW+'\n[+] SSH Bruteforce Started... This Might Take A While!!!'+Fore.WHITE)
                 mps_scan = subprocess.check_output(f'nmap -sV --script={f.split(".")[0]} {tar} -Pn\n', shell=True).decode()
                 print(Fore.YELLOW+'\n[+] MapSploit Scan Completed...\n'+Fore.WHITE)
                 print(Fore.RED+mps_scan+Fore.WHITE)
                 if 'Invalid argument' in mps_scan:
                    print(Fore.YELLOW+f'\n[+] Invalid Ip Address Was Provided!!!\nInvalid Host ------> {tar}'+Fore.WHITE)
      elif console == 'exit':
           print(Fore.GREEN+'\n[+] Exiting MapSploit...\n'+Fore.WHITE)
           break
           exit(0)
      elif console == 'update script':
           print(Fore.YELLOW+'\n[+] Updating MapSploit Scripts...'+Fore.WHITE)
           update = subprocess.check_output('nmap --script-updatedb', shell=True).decode()
           print(Fore.GREEN+'\n[+] MapSploit Script Is Up To Date'+Fore.WHITE)
      elif console == 'scan port':
           target = open('target.txt', 'r').read()
           print(Fore.YELLOW+f'\n[+] Scanning For Open Port In {target}\n'+Fore.WHITE)
           pt_scan = subprocess.check_output(f'nmap {target} -Pn', shell=True).decode()
           print(Fore.RED+pt_scan+Fore.WHITE)
      else:
           print(Fore.YELLOW+'\n[+] Type (help) for mapsploit command'+Fore.WHITE)
