# THIS IS A SIMPLE PYTHON CODE FOR BULK GENERATING V2RAY USERS [VMESS & VLESS] ON X-UI 
## DON'T STEAL MY SHIT, OR I'LL KICK YOUR ASS
### THIS CODE IS FREE AS HELL, DON'T SELL THIS CRAP 
#### I'VE NO AFFILIATION WITH X-UI 
##### IF YOU DON'T KNOW WHAT THE FUCK ARE YOU DOING, DON'T USE THIS CODE
###### THIS CODE DELETES YOUR X-UI DATABASE WITH ALL ITS USERS AND CONTENT
####### I'M NOT RESPONSIBLE IF YOU STARTED A NUCLEAR WAR OR YOU GOT FIRE BY USING THIS CODE 
######## MAKE SURE YOU'VE x1.db FILE and x-ui.db FILES RIGHT HERE IN THIS VERY DIRECTORY!
######### THIS IS A DUMMY LINE, CAUSE I LIKE WRITING COMMENTS ON MY CODES
########## FOLLOW ME ON TWITTER: HTTPS://TWITTER.COM/NO_ITSMYTURN 

import os
import sqlite3
import shutil
import random
import uuid
import json
import base64
print("\n\n")
print("THIS PYTHON FILE NEEDS TO BE AT THE SAME DIRECTORY AS THE x-ui.db")
print("WHICH IS HERE: /etc/x-ui/")
print("----------")
print("How many and what?\nThis is the format you gotta write:")
print("100:vmess\nor 100:vless\nor for mixed accounts:\n60:vless,40:vmess")
numbers = input("Write your answer and press return: ")
with open("ports.txt","w") as f: f.write("")
print("Now tell me your remark \n(it will be used as user's connection name) (e.g. BlahVPN)")
remark0 = input().split("\n")[0]
print("Enter server IP or your cloudflare's proxied subdomain (without HTTP or HTTPS)")
ip = input("")
bw = input("How much would be each account's limit? write in GB without GB (e.g. 1 or 10): ")
bw = int(bw) * 1073741824
def inject(code):
    try:
     
        sqliteConnection = sqlite3.connect('x-ui.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = code

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Inserted")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Connection closed")
def portgen():
    port = random.choice(range(11111,62999))
    with open("ports.txt","a+") as f:
        if port != 54321:
            f.write(str(port))
            f.write("\n")
vlessnum = 0 
vmessnum = 0
if "vmess" in numbers and "vless" not in numbers: 
    vmessnum = numbers.split(":")[0]

elif "vless" in numbers and "vmess" not in numbers: 
    vlessnum = numbers.split(":")[0]
elif "vless" in numbers and "vmess" in numbers:
    vl = numbers.split(",")[0]
    vm = numbers.split(",")[1]
    vlessnum = vl.split(":")[0]
    vmessnum = vm.split(":")[0]
numports = int(vlessnum) + int(vmessnum)
print("You want %s VLESS and %s VMESS" %(vlessnum,vmessnum))
print("Let's begin..")
if os.path.exists("x-ui.db"):
    os.remove("x-ui.db")
with open("vmess.txt","w") as f: f.write("")
with open("vless.txt","w") as f: f.write("")
print("x-ui.db has been removed..")
shutil.copyfile("x1.db", "x-ui.db")    
print("x1.db sample has been copied..")
print("Now I've to generate %s random ports!"%(numports))
for i in range(0,numports):
    portgen()
print("Ports generated\nNow let's clean the repetitive ports!")
uniqlines = set(open('ports.txt').readlines())
with open('ports.txt', 'w') as bar:
    bar.writelines(uniqlines)
print("Done")
with open('ports.txt') as f: totalports = len(f.readlines())
with open('ports.txt') as f: plist = f.readlines()
print("Now there are %s unique ports"%(totalports))
for i in range(0,totalports):
    if i < int(vlessnum):
        try:
            port = plist[i].split("\n")[0]
            print(port)
            myuuid = uuid.uuid4()
            remark1 = str(remark0) + "-" + str(random.choice(range(0,1000000)))
            vless = """INSERT or IGNORE INTO inbounds VALUES ('%s', '1', '0', '0', '%s', '%s', '1', '0', '', '%s', 'vless', '{\n    "clients": [\n        {\n        "id": "%s",\n        "flow": "xtls-rprx-direct"\n        }\n    ],\n    "decryption": "none",\n    "fallbacks": []\n    }', '{\n    "network": "ws",\n    "security": "none",\n    "wsSettings": {\n        "path": "/",\n        "headers": {}\n    }\n    }', '%s', '{\n    "enabled": true,\n    "destOverride": [\n        "http",\n        "tls"\n    ]\n    }');"""%(i,bw,remark1,port,myuuid,f"inbound-{port}")
            inject(vless)
            linkk = "vless://" + str(myuuid)  + "@" + str(ip) + ":" + str(port) + "?type=ws&security=none&path=/#" + str(remark1)
            with open("vless.txt","a+") as f:
                f.write(str(linkk) + "\n")
        except:pass
    else:
        try:
            port = plist[i].split("\n")[0]
            myuuid = uuid.uuid4()
            remark1 = str(remark0) + "-" + str(random.choice(range(0,1000000)))
            vmess = """INSERT INTO "inbounds" VALUES ('%s', '1', '0', '0', '%s', '%s', '1', '0', '', '%s', 'vmess', '{\n    "clients": [\n        {\n        "id": "%s",\n        "alterId": 0\n        }\n    ],\n    "disableInsecureEncryption": false\n    }', '{\n    "network": "ws",\n    "security": "none",\n    "wsSettings": {\n        "path": "/",\n        "headers": {}\n    }\n    }', 'inbound-%s', '{\n    "enabled": true,\n    "destOverride": [\n        "http",\n        "tls"\n    ]\n    }')""" %(i,bw,remark1,port,myuuid,port)
            inject(vmess)
            config = {
            "v": "2",
            "ps": remark1,
            "add": ip,
            "port": port,
            "id": str(myuuid),
            "aid": 0,
            "net": "ws",
            "type": "none",
            "host": "",
            "path": "/",
            "tls": "none"
            }
            config = json.dumps(config)
            e1 = base64.b64encode(config.encode("utf-8"))
            e2 = str(e1, "utf-8")        
            linkk = "vmess://" + e2    
            with open("vmess.txt","a+") as f:
                f.write(str(linkk) + "\n")
        except:pass
print("Done!\nCheck vless.txt && vmess.txt\nAlso run this: x-ui restart\n-----------")
print("Finally:\nYour X-UI panel has changed now, port will be 991, username and password will be 'admin', change them after logging in")
