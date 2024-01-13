import requests,os,sys,random,re,time
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup as parse
from rich.panel import Panel as nel
from rich import print as cetak
from rich.tree import Tree 
from fake_email import Email

try:
  import getpass
except ImportError:
  print("[*] Sedang Install Module getpass");time.sleep(0.1)
  os.system("pip install getpass")
  
def back():
	menu(cok)
	
def language(cookie):
  try:
    xyz = requests.Session()
    req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
    pra = bs(req.content,'html.parser')
    for x in pra.find_all('form',{'method':'post'}):
      if 'Bahasa Indonesia' in str(x):
        bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"submit"  : "Bahasa Indonesia"}
        exec = xyz.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
    
  except Exception as e:pass
def logo():
	cetak(nel(''' [b green]● [b yellow]●[b red] ●[b white]
  _________________________________ 
  \_   _____/\__    ___/\_   _____/     Code By : Atsuna-ID
   |    __)    |    |    |    __)   Tools : Facebook Tools Free
   |     \     |    |    |     \    
   \___  /     |____|    \___  /    
       \/                    \/     ''',style="b blue",title=f'[b red] Banner'))

def login():
	try:
		cok = open("kue.txt",'r').read()
		print("Cookies Loading")
	except IOError:
		cok = input("Masukan Cookie: ")
		open("kue.txt","w").write(cok)
		print("Cookies tersimpan di file")
	menu()
def menu():
	try:
		os.system("clear")
		cok = open("kue.txt","r").read()
	except IOError:
		print("Jika Tidak Berhasil Ganti Coki")
	logo()
	cetak(nel(f"[white][1] Add Email\n[2] Ubah Email Utama\n[3] Hapus Email\n[4] Hapus Teman\n[5] Ganti Password\n[6] Keluar Dari Group\n[C] Cek Info Tools",style='b blue',title='[b red] Menu Tools [white]'))
	xzy = input("  [?] Pilih : ")
	if xzy in ["1","01"]:add(cok)
	elif xzy in ["2","02"]:ubah(cok)
	elif xzy in ["3","03"]:hps(cok)
	elif xzy in ["4","04"]:teman(cok)
	elif xzy in ["5","05"]:pw(cok)
	elif xzy in ["6","06"]:group(cok)
	elif xzy in ["C"]:CEK()
def CEK():
	tree = Tree("Information Tools")
	tree.add("[Yayan XD]")
	tree.add("[Fanda]")
	tree.add("[Rahma Saputra]")
	tree.add("[Rizky Nurahman]")
	tree.add("[Errucha Cuyy]")
	tree.add("[Rafi Khalbi]")
	tree.add("[Georgy Alifich L Zhukov ZV]")
	tree.add("[Rohmat Basuki XD]")
	tree.add("[Tamsis XXX]")
	tree.add("[Atsuna-ID]")
	cetak(nel(tree))
	
def head():
  return{'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',}
	
def add(cok):
	pw = getpass.getpass("  [*] Masukan Pass : ")
	create = Email().Mail()
	email = create['mail']
	email_post = create['mail']
	email_ses = create["session"]
	uri = par(requests.get(f"https://mbasic.facebook.com/settings/email/add",cookies={"cookie":cok}).text, "html.parser")
	form = uri.find('form', {'method': 'post'})
	data = {
				"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
				'jazoest'   : re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
				'email': email,
				'add_email': re.search('name="add_email" type="hidden" value="(.*?)"',str(form)).group(1),
				"qp_id": "",
				"c": "",
				"qp_h": "",
				"source_added": "",
				"save_password": pw,
				"save": re.search('name="save" size="0" type="submit" value="(.*?)"', str(form)).group(1),
				}
	url = "https://mbasic.facebook.com"+re.search('action="(.*?)"',str(form)).group(1)
	po = par(requests.post(url,data=data,cookies={"cookie": cok}).text, "html.parser")

	if "Menunggu Persetujuan" in str(po):
		print(f"  [*] Email Berhasil di Buat: {email}")
		url_code = re.search('a href="/entercode.php(.*?)"',str(po)).group(1).replace('amp;','')
		
		konfir(cok,url_code,email_ses,email_post)
	elif "Anda DiBlokir Sementara" in str(po):
		print("Akun Anda Spam")
	else:
		print("Gagal")
def konfir(cok,url_code,email_ses,email_post):
	link = requests.get(f"https://mbasic.facebook.com/entercode.php"+url_code,cookies={"cookie": cok}).text
	soup1 = par(link, "html.parser")
	form1 = soup1.find("form", {"method": "post"})
	while True:
		mass=Email(email_ses).inbox()
		if mass:
			code = re.search('konfirmasi ini: (.*?).<',mass['message']).group(1)
			OTP = (' otp : '+re.search('konfirmasi ini: (.*?).<',mass['message']).group(1))
			break
	data1= {
				'code': code,
				'email': email_post,
				"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form1)).group(1),
				'jazoest'   : re.search('name="jazoest" type="hidden" value="(.*?)"', str(form1)).group(1),
				
				}
	url = "https://mbasic.facebook.com"+re.search('action="(.*?)"',str(form1)).group(1)
	pos = par(requests.post(url,data=data1,cookies={"cookie":cok}).text, "html.parser")
	if "Anda Diblokir Sementara" in str(pos):
		print("  [>]  Email Gagal Di Konfirmasi")
	else:
		print(f"  [*] Kode Konfirmasi: {code}\n  [?] OTP Konfirmasi: {OTP}\n  [*] Berhasil Di Konfirmasi: {email_post}")
		kembali()
	
	
def ubah(cok):
	hos = requests.get("https://mbasic.facebook.com/settings/email",cookies={"cookie": cok}).text
	soup = bs(hos, "html.parser")
	x = re.findall('\<span class="ce cf">(.*?)<\/span>',str(soup))
	for i , email in enumerate(x, 0):pass
	ouput = "\n".join([f"{i}. {email}" for i, email in enumerate(x, 0)])
	cetak(nel(ouput, title="Daftar Email"))
	user  = input("  [?] Masukan Email Yg Ad Di Fb Nya\n  [*] Masukan Email : ")
	email = user.split(",")
	url = requests.get("https://mbasic.facebook.com/settings/email/?primary_email",cookies={"cookie":cok}).text
	soup = bs(url, "html.parser")
	form = soup.find("form", {"method": "post"})
	data = {
		"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
		'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
		"email": email,
		"change_primary": '1',
		'save': re.search('name="save" size="0" type="submit" value="(.*?)"', str(form)).group(1)
		}
	link = "https://mbasic.facebook.com"+re.search('action="(.*?)"',str(form)).group(1)
	post = bs(requests.post(link,data=data,cookies={"cookie": cok}).text, "html.parser")
	if "Anda Diblokir Sementara" in str(post):
		print("  [?] Gagal Mengubah Email Utama")
		kembali()
	else:
		mal = re.findall('\<span class="cj">(.*?)<\/span>',str(post))
		email = ",".join(mal)
		cetak(nel(f"  [*] Email Utama Saat Ini: {email}",style='b blue',title='[b green]Selamat Berhasil[white]'))
		kembali()

def hps(cok):
    url = f"https://mbasic.facebook.com/settings/email"
    get = requests.get(url,cookies={'cookie':cok})
    sup = bs(get.text, 'html.parser')
    #print(sup.prettify())
    html = re.findall('\<span class="ce cf">(.*?)<\/span>', str(sup))
    #print(sup.prettify())
    for i , email in enumerate(html, 0):pass
    x = "\n".join([f'{i}. {email}' for i, email in enumerate(html, 0)])
    cetak(nel(f"{x}",title='b white Daftar email',style='b blue'))
    mail = input("  [*] Masukan Email: ")
    password = input("  [?] Silahkan Pilih (Y/T) Jika Sandi Diperlukan\n  [*] Pilih: ")
    if password =="y":
      pw = input("  [*] Masukan Pass: ")
      
    link = f"https://mbasic.facebook.com/settings/email/?remove_email&email={mail}"
    url = requests.get(link,cookies={"cookie":cok})
    soup = bs(url.text,"html.parser")
    form = soup.find("form", {"method": "post"})
    if password =="y":
      data = {
            "fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
            'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
            'remove_email': "1",
            "email": mail,
            'save_password': pw,
            'error_uri': f"/settings/email/?remove_email&amp;email={mail}",
            'save': "Hapus Email"
            }
    elif password =="t":
      data = {
            "fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
            'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
            'remove_email': "1",
            "email": mail,
            'error_uri': f"/settings/email/?remove_email&amp;email={mail}",
            'save': "Hapus Email"
            }
    pos = requests.post('https://mbasic.facebook.com'+form['action'],data=data,cookies={"cookie": cok}).text
    
    if "Perubahan Disimpan" in str(pos):
        print(f"  [*] Email Berhasil Dihapus: {mail}")
        time.sleep(2)
        kembali()
    else:
        print("  [?] Gagal Menghapus Email")
        time.sleep(2)
        kembali()

def kembali():
	print("  [*] Lanjut Apa Tidak(T/Y)")
	woi = input("  [?] PILIH : ")
	if woi in ["y","Y"]:
		menu()
	else:
		print("  [*] Terima Kasih By : Atsuna-ID")
		time.sleep(2)
		exit()
		

if __name__=="__main__":
	os.system("clear")
	login()
	languege(cookie)
	
