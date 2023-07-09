import os
import subprocess
from colorama import Fore, Style
fileName = '/etc/issue'
bashFile = 'scripts/loginMod.sh'
banner_text = """WARNING: Unauthorized access to this system is prohibited.
By accessing this system, you agree that your actions may be monitored and recorded."""
bashFileCommand = ["bash", bashFile]
desired_string = "Ubuntu 22.04"
def localLogingWarning():
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
            content = ''.join(lines)
        file.close()
        if (banner_text in content):
            print(Fore.GREEN + "\n\033[1m[+] Local Login Warning Banner change FAILED: banner seems to be changed" + Style.RESET_ALL)
        else:
            if any(desired_string in line for line in lines):
                modifyFiles()
            else:
                print(Fore.RED + "\n\033[1m[-] Local Login Warning Banner change FAILED: error file seems to be changed" + Style.RESET_ALL)
    else:
        print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error file not found' + Style.RESET_ALL)

def modifyFiles():
    try:
        with open(fileName, 'w') as file:
            file.write(banner_text)
        file.close()
        process = subprocess.Popen(bashFileCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(Fore.GREEN + '\n\033[1m[+] Local Login Warning Banner change SUCCESS: banner changed!' + Style.RESET_ALL)
        else:
            print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error something went wrong' + Style.RESET_ALL)
            print(stderr.decode("utf-8"))
    except:
        print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error something went wrong' + Style.RESET_ALL)