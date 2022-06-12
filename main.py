import os
import time
import requests
from os.path import exists
from time import sleep
from colorama import Fore, Style, init

if os.path.exists("tokens.txt") == False:
    with open("tokens.txt", 'w') as f:
        f.write("put ur tukenz here")
        print("Relanuch this and put your tokens in tokens.txt!")
        time.sleep(3)
        quit() 
with open('tokens.txt', 'r') as fp:
    tokenamm = len(fp.readlines())
    if tokenamm == 0:
        print("please put tokens in tokens.txt!")
        time.sleep(3)
        quit()
    print(f"Loaded {tokenamm} Tokens!")
    time.sleep(3)
    os.system('cls')

start = input(Fore.MAGENTA + """


                                ██████╗  █████╗ ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                                ██╔══██╗██╔══██╗██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                                ██████╔╝███████║██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
                                ██╔══██╗██╔══██║██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
                                ██║  ██║██║  ██║██║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                  


                                                    1: raid tool
                                                       2: exit
                                                    Made by ! Harvey
                                                        => """)
if start == '2':
          quit()
elif start == '1':
          chan = input("What is the channel id? ")
          amm = int(input("How many messages do you want? "))
          message = input("What should the message be? ")
          def sendMessage(token, channel_id, message):
                url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
                data = {"content": message}
                header = {"authorization": token}
 
                r = requests.post(url, data=data, headers=header)

                if r.status_code == 429:
                    print("Rate limited please wait!")
                elif r.status_code == 200:
                    print("Sent " + message)
                else:
                    print("Invalid token or channel id!")          
          with open("tokens.txt", "r", encoding="utf-8") as f:
              file_token = f.read().split("\n")
              tokens = []
              for x in file_token:
                  if x != "": tokens.append(x)    
          while amm > 1:
            x = 0
            amm = amm - 1
            for i in range(tokenamm):    
                sendMessage(tokens[x], chan, message)             
                x = x + 1
