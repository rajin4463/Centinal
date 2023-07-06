import subprocess
import time
from colorama import Fore, Style

x = 1

def telnet():
    compare = "telnet	install ok installed	installed"
    command = "dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' telnet"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')

    if compare in output:
        print(Fore.RED + "\n\033[1m[+] telnet client was found.")
        print("\n\033[1m[-] Purging client" + Style.RESET_ALL)
        purgeCommand = ["apt-get", "purge", "-y", "telnet"]
        process = subprocess.run(purgeCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        animation()
        if process.returncode == 0:
            x = 0
            print(Fore.GREEN + "\n\033[1m[+] Successfully purged Telnet Client." + Style.RESET_ALL)
        else:
            print(Fore.RED + "\n\033[1m[-]telnet client purge FAILED: error something went wrong\n" + Style.RESET_ALL)
            print(result.stderr.decode("utf-8"))
    else:
        print(Fore.RED + "\n\033[1m[-]telnet client purge FAILED: error telnet client dosen't seem to be installed.")
        print(output)

def animation():
    animation = "|/-\\"
    idx = 0
    while x==1:
        print(Fore.GREEN + '...' + animation[idx % len(animation)], end="\r" + Style.RESET_ALL)
        idx += 1
        time.sleep(0.1)