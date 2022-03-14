import requests,re,time,os,random
from bs4 import BeautifulSoup as bs
save  = []
os.system("clear")
try:
    grey = '\x1b[90m'
    red = '\x1b[91m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    blue = '\x1b[94m'
    purple = '\x1b[95m'
    cyan = '\x1b[96m'
    white = '\x1b[37m'
    flag = '\x1b[47;30m'
    off = '\x1b[m'
except:
	pass

def img():
	x = f"""Author : hudaxcode
Tools  : buat downloads image waifumu..
{red}___________           .__          
\__    ___/___   ____ |  |   ______
  |    | /  _ \ /  _ \|  |  /  ___/
  |    |(  <_> |  <_> )  |__\___ \ 
  |____| \____/ \____/|____/____  {off}> version {grey}2.0{red}
                                \/ {off}"""
	print(x)

def menu():
	img()
	print(f" 1. source wallpapercave.com")
	print(f" 2. source printart.com [{red}maintance{off}]")
	hx = input("hudaxcode: ")
	if hx =="1":
		search()

def search():
	global search
	num = 1
	search = input(f"query wifumu({green}kurumi{off}): ")
	s      = search.replace(" ","+")
	url    = f"https://wallpapercave.com/search?q={s}"
	get    = requests.get(url).text
	hxc    = bs(get,'html.parser')
	zt     = hxc.findAll("a")
	ztt    = re.findall('<div class="albumphoto" href="(.*?)"',str(zt))
	zttt   ="".join(ztt)
	with open("hudaxcode","a") as hxc:
		hxc.write(zttt.replace("/","\n"))
	z      = re.findall('p class="number">(.*?)</p>',str(zt))
	print(f"results for query {green}{search}{off}....")
	for a in z:
		print(f"[{num}]. {yellow}{a}{off}")
		num +=1
	op  = open("hudaxcode").readlines()
#	print(f"\ntype '{green}all{off}' untuk mendownloads semua image")
#	print(f"type '{green}1,2{off}' untuk mengabungkan mendownloads  image")
	x   = input("hudaxcode: ")
	url = op[int(x)]
	get_url(url.replace("\n",""))

def get_url(url):
	print("please wait, Getting data..")
	urlku = f"https://wallpapercave.com/mwp/"
	urlme = f"https://wallpapercave.com/{url}"
	hxc   = requests.get(urlme).text
	if not 'source media' in hxc:
		hxc1  = bs(hxc,'html.parser')
		for index in re.findall('<a class="download" href="(.*?)"',str(hxc1)):
			save.append(index)
		downloads()
	elif 'source media' in hxc:
		hxc1  = bs(hxc,'html.parser')
		hxc2  = hxc1.findAll("source")
		for index in re.findall('srcset="/mwp/(.*?)"',str(hxc2)):
			save.append(index)
		downloads()

def downloads():
	global search
#	urlku = "https://wallpapercave.com/mwp/"
	urlku = "https://wallpapercave.com"
	loads = 1
	print(f"Total data foto di dapatkan {red}{len(save)}{off}")
	folder = input(f"Masukan folder save downloads( {green}/sdcard/Download/{search}{off} )\nhudaxcode: ")
	try:os.system(f"mkdir {folder}")
	except:pass
	print(f"{cyan}Starting downloads...{off}")
	if not "download" in save:
		for hxc in save:
			print(f"{loads}. {green}{urlku}{hxc} downloads √{off} ")
			urlme = f"{urlku}{hxc}"
			response = requests.get(urlme)
			if response.status_code == 200:
				with open(f"{folder}/{loads}.png", 'wb') as f:
					f.write(response.content)
			loads += 1

	elif "download" in save:
		tok = "https://wallpapercave.com/"
		tok1 = "https://wallpapercave.com/wp/"
		for hxc in save:
			print(f"{loads}. {green}{tok}{hxc} downloads √ {off}")
			urlme = f"{tok1}{hxc}"
			response = requests.get(urlme)
			if response.status_code == 200:
				with open(f"{folder}/{loads}.png", 'wb') as f:
					f.write(response.content)
			loads += 1



if __name__=="__main__":
	os.system("rm -rf hudaxcode")
	menu()
