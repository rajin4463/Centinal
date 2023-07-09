import os
from colorama import Fore, Style
fileName = '/etc/issue'
bashFile = '~/.bashrc'
banner_text = """WARNING: Unauthorized access to this system is prohibited.
By accessing this system, you agree that your actions may be monitored and recorded."""
bashFileCommand = "cat /etc/issue"
desired_string = "Ubuntu 22.04"
def localLogingWarning():
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
        file.close()
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
        with open(bashFile, 'a') as file:
            file.write(bashFileCommand)
        file.close()
        print(Fore.GREEN + '\n\033[1m[+] Local Login Warning Banner change SUCCESS: banner changed!' + Style.RESET_ALL)
    except:
        print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error something went wrong' + Style.RESET_ALL)