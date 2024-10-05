import socket
import os
import sys
from Tools.nmap_script import *
from Tools.msf_script import *
from Tools.hxs_script import *

class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    PURPLE = '\033[35m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = "\033[01;01m"
    DARK_RED = "\033[38;5;124m"
    CRIMSON = "\033[38;5;196m"
    TOMATO = "\033[38;5;202m"
    LIGHT_RED = "\033[91m"

terminal = TextColors.CRIMSON + "AKIRA > "  + TextColors.RESET

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.CRIMSON + """
 ▄▄▄       ██ ▄█▀ ██▓ ██▀███   ▄▄▄      
▒████▄     ██▄█▒ ▓██▒▓██ ▒ ██▒▒████▄    
▒██  ▀█▄  ▓███▄░ ▒██▒▓██ ░▄█ ▒▒██  ▀█▄  
░██▄▄▄▄██ ▓██ █▄ ░██░▒██▀▀█▄  ░██▄▄▄▄██ 
 ▓█   ▓██▒▒██▒ █▄░██░░██▓ ▒██▒ ▓█   ▓██▒
 ▒▒   ▓▒█░▒ ▒▒ ▓▒░▓  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
  ▒   ▒▒ ░░ ░▒ ▒░ ▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░
  ░   ▒   ░ ░░ ░  ▒ ░  ░░   ░   ░   ▒   
      ░  ░░  ░    ░     ░           ░  ░
          
-- AKIRA HACKING TOOLS --
-- BACKDOOR CREATER --
-- github : github.com/madanokr001 --
-- Version 1.0 --
-- use www.revshells.com -- 
          
[1] NMAP
[2] MSFVENOM
[3] HoaxShell
[4] EXIT  
              
    """ + TextColors.RESET)

def main():
        while True:
            logo()
            select = input(TextColors.CRIMSON + terminal + TextColors.RESET)

            if select == "1" or select == "nmap":
                nmap()

            if select == "2" or select == "m":
                msfvenom()
                
            if select == "3" or select == "hoax":
                hoaxshell()
                

            if select == "4" or select == "exit":
                print(TextColors.YELLOW + "[-] AKIRA EXIT..."+ TextColors.RESET)
                sys.exit()
    
        
                    

                


        


if __name__ == "__main__":
    main()
