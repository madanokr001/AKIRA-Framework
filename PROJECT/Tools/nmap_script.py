import os

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
    ESET = '\033[0m'
    BOLD = "\033[01;01m"
    DARK_RED = "\033[38;5;124m"
    CRIMSON = "\033[38;5;196m"
    TOMATO = "\033[38;5;202m"
    LIGHT_RED = "\033[91m"

def nmap():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.CRIMSON +"""
 ███▄    █  ███▄ ▄███▓ ▄▄▄       ██▓███  
 ██ ▀█   █ ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒
▓██  ▀█ ██▒▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒
▓██▒  ▐▌██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒
▒██░   ▓██░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░
░ ▒░   ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
░ ░░   ░ ▒░░  ░      ░  ▒   ▒▒ ░░▒ ░     
   ░   ░ ░ ░      ░     ░   ▒   ░░       
         ░        ░         ░  ░   
             
-- version 1.0 -- 
-- nmap 7.95 --   

[1] INSTALL NMAP          
[2] NMAP 7.95
[3] CHEATSHEET
          
          """)

    while True:

        select = input(TextColors.CRIMSON + "AKIRA > " + TextColors.ESET)

        if select == "2" or select.lower() == "nmap":
            target = input(TextColors.CRIMSON + "[+] IP : "+ TextColors.ESET)
            flags = input(TextColors.CRIMSON + "[+] FLAGS : "+ TextColors.ESET)
            os.system(f"nmap {target} {flags}")


        elif select == "3" or select.lower() == "cheat":
            print(TextColors.CRIMSON +"""
NMAP COMMANDS

SINGLE TARGET SCAN
NMAP [TARGET]

MULTIPLE TARGET SCAN
NMAP [TARGET1,TARGET2,...]

SCAN FROM LIST OF TARGETS
NMAP -IL [LIST.TXT]

SCAN A RANGE OF HOSTS
NMAP [IP_RANGE]

FULL SUBNET SCAN
NMAP [IP/CIDR]

SCAN RANDOM HOSTS
NMAP -IR [NUMBER]

EXCLUDE TARGET FROM SCAN
NMAP [TARGET] --exclude [TARGET]

EXCLUDE TARGETS USING A LIST
NMAP [TARGET] --excludefile [LIST.TXT]

PERFORM AGGRESSIVE SCAN
NMAP -A [TARGET]

SCAN IPV6 TARGETS
NMAP -6 [TARGET]

DISCOVERY OPTIONS

NMAP QUERY

PING SCAN ONLY
NMAP -SP [TARGET]

DO NOT SEND PING
NMAP -PN [TARGET]

TCP SYN PING
NMAP -PS [TARGET]

TCP ACK PING
NMAP -PA [TARGET]

UDP PING
NMAP -PU [TARGET]

SCTP INIT PING
NMAP -PY [TARGET]

ICMP ECHO PING
NMAP -PE [TARGET]

ICMP TIMESTAMP PING
NMAP -PP [TARGET]

ICMP ADDRESS MASK PING
NMAP -PM [TARGET]

IP PROTOCOL PING
NMAP -PO [TARGET]

ARP PING
NMAP -PR [TARGET]

TRACEROUTE
NMAP --traceroute [TARGET]

FORCE REVERSE DNS RESOLUTION
NMAP -R [TARGET]

DISABLE REVERSE DNS RESOLUTION
NMAP -N [TARGET]

USE ALTERNATIVE DNS QUERY
NMAP --system-dns [TARGET]

MANUALLY SPECIFY DNS SERVERS
NMAP --dns-servers [SERVER] [TARGET]

CREATE HOST LIST
NMAP -SL [TARGET]

FIREWALL EVASION TECHNIQUES

NMAP QUERY

PACKET FRAGMENTATION
NMAP -F [TARGET]

SPECIFY MTU
NMAP --mtu [MTU] [TARGET]

USE DECoys
NMAP -D RND:[NUMBER] [TARGET]

IDLE ZOMBIE SCAN
NMAP -SI [ZOMBIE] [TARGET]

MANUALLY SPECIFY SOURCE PORT
NMAP --source-port [PORT] [TARGET]

ADD RANDOM DATA
NMAP --data-length [SIZE] [TARGET]

RANDOMIZE TARGET SCAN ORDER
NMAP --randomize-hosts [TARGET]

SPOOF MAC ADDRESS
NMAP --spoof-mac [MAC|0|VENDOR] [TARGET]

SEND INVALID CHECKSUM
NMAP --badsum [TARGET]

VERSION DETECTION

NMAP QUERY

OPERATING SYSTEM DETECTION
NMAP -O [TARGET]

GUESS UNKNOWN
NMAP -O --osscan-guess [TARGET]

SERVICE VERSION DETECTION
NMAP -SV [TARGET]

TROUBLESHOOT VERSION SCAN
NMAP -SV --version-trace [TARGET]

PERFORM RPC SCAN
NMAP -SR [TARGET]

OUTPUT OPTIONS

NMAP QUERY

SAVE OUTPUT TO TEXT FILE
NMAP -oN [SCAN.TXT] [TARGET]

SAVE OUTPUT TO XML FILE
NMAP -oX [SCAN.XML] [TARGET]

GREP-ABLE OUTPUT
NMAP -oG [SCAN.TXT] [TARGET]

OUTPUT ALL FILE TYPES
NMAP -oA [PATH/FILE_NAME] [TARGET]

DISPLAY STATS PERIODICALLY
NMAP --stats-every [TIME] [TARGET]

SILENT OUTPUT
NMAP -oS [SCAN.TXT] [TARGET]

SCRIPTING ENGINE

NMAP QUERY

RUN INDIVIDUAL SCRIPT
NMAP --script [SCRIPT.NSE] [TARGET]

RUN MULTIPLE SCRIPTS
NMAP --script [EXPRESSION] [TARGET]

RUN SCRIPTS BY CATEGORY
NMAP --script [CAT] [TARGET]

RUN MULTIPLE SCRIPT CATEGORIES
NMAP --script [CAT1,CAT2,...] [TARGET]

TROUBLESHOOT SCRIPT
NMAP --script [SCRIPT] --script-trace [TARGET]

UPDATE SCRIPT DATABASE
NMAP --script-update-db
                  
                """)
            input("")
            nmap()
            
        elif select == "1" or select.lower() == "install":
            os.system(f"apt-get install nmap")

            





    

