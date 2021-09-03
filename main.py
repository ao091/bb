import sys
import os

def Login(theprint = True):
    global fini
    if(theprint):
        spinner.start("Logging into account\n")
    global session    
    session = requests.Session()
   
    
    checkemail = requests.session("https://login.live.com/GetCredentialType.srf",verify=False,headers=headers)
    
with open('log.txt, r') as f:
	accounts_list = f.readlines()

for account in accounts_list:
	print(account.strip())
   
if not keyExist(session.cookies,'PPAuth'):
        sys.exit("Couldn't log in")
