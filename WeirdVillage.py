from nmap import PortScanner
import requests
import json
from colorama import Fore,init
import random
import os
import base64
from tqdm import tqdm
import sys
import time
import platform
from pyExploitDb import PyExploitDb
import nmap
import socket
import time
from scapy import *
import sqlite3
from pystyle import Colors, Colorate
import json
from googlesearch import search
import stepic
from PIL import Image
from faker import Faker
import webbrowser
import urllib3
from bs4 import BeautifulSoup
from playsound import playsound
import numpy as np
import cv2

init()

usernamess = os.getlogin()
usernamess.strip()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

maintext = ("""


 .d888888           oo dP                   
d8'    88              88                   
88aaaaa88a .d8888b. dP 88 .d8888b. 88d888b. 
88     88  88'  `88 88 88 88'  `88 88'  `88 
88     88  88.  .88 88 88 88.  .88 88       
88     88  `8888P88 dP dP `88888P8 dP       
oooooooooooo~~~~.88~oooooooooooooooooooooooo
            d8888P                          
Created By @PessareKhiyabon From WeirdVillage !
""")

hprint(Fore.YELLOW+"["+Fore.CYAN+" + "+Fore.YELLOW+"]"+Fore.BLUE+color.BOLD+" Loading The Agilar........... ")
print(Colorate.Horizontal(Colors.rainbow, maintext))

print("\n")

print(Fore.CYAN+"["+Fore.YELLOW+" Warning ! "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" > Please Use a VPn For Better Attacking...")
print(Fore.CYAN+"["+Fore.BLUE+" Info "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" > Enter Vlid Domain Example google.com \n")
import pystyle







resdnss = input(Fore.CYAN+"["+Fore.BLUE+" Enter  "+Fore.CYAN+"]"+Fore.YELLOW+color.BOLD+" > Domain : ")
hprint(Fore.CYAN+"[ "+Fore.BLUE+resdnss+Fore.CYAN+" ]"+Fore.GREEN+color.BOLD+" > OK! Scaning The Domain Please Wait Dont Close.....\n")
# ارسال درخواست به وب‌سایت و دریافت پاسخ
url = "https://"+resdnss
response = requests.get(url)
# استخراج نام دامنه از URL
domain_name = url.split("//")[-1].split("/")[0]

# استفاده از BeautifulSoup برای تجزیه HTML
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج عنوان وب‌سایت
title = soup.find('title').text
hprint(Fore.CYAN+"["+Fore.BLUE+" Title "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+"\n")
print(title)
print(Fore.CYAN+"["+Fore.YELLOW+" DNS Records "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" ")
resdns = requests.get("https://api.hackertarget.com/dnslookup/?q="+resdnss).text
print(Fore.YELLOW+resdns)






ipsite = socket.gethostbyname(resdnss)
ipsite = ipsite.strip()



print("\n")
print(Fore.CYAN+"["+Fore.YELLOW+" Wordpress 5 Page Attack "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" ")

wordi = requests.get("https://"+resdnss+"/wp-admin")
if wordi.status_code == 200:
    
    print(Fore.CYAN+"["+Fore.BLUE+" WP Admin "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" https://"+resdnss+"/wp-admin "+Fore.CYAN+"200 OK!")
    
else :
    
    print(Fore.CYAN+"["+Fore.BLUE+" WP Admin "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" https://"+resdnss+"/wp-admin "+Fore.CYAN+"400 NOTFOUND")

wordi = requests.get("https://"+resdnss+"/wp-json/wp/v2/users")
if wordi.status_code == 200:
    
    print(Fore.CYAN+"["+Fore.BLUE+" WP Users List "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" https://"+resdnss+"/wp-json/wp/v2/users "+Fore.CYAN+"200 OK!")
    
else :
    
    print(Fore.CYAN+"["+Fore.BLUE+" WP Admin "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" https://"+resdnss+"/wp-admin "+Fore.CYAN+"400 NOTFOUND")


scanner = PortScanner()

IP = (ipsite)
#port_range = input("[*]PORT RANGE (Example : 20-80) : ")
print("\n")
print(Fore.CYAN+"["+Fore.YELLOW+" DDOS Ports "+Fore.CYAN+"]"+Fore.GREEN+color.BOLD+" ")

scanner.scan(IP , ports='80,21,3389,8080,443,25,2083,22,53')

open_tcp_ports = scanner[IP]["tcp"].keys()

print("------------")
for port in open_tcp_ports:
    service_name = scanner[IP]["tcp"][port]["name"]
    print ("{} - {} : OPEN".format(port , service_name))







