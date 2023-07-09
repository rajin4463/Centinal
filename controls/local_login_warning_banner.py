import os
from colorama import Fore, Style
fileName = '/etc/issue'
banner_text = """\nWARNING: Unauthorized access to this system is prohibited.
By accessing this system, you agree that your actions may be monitored and recorded.
"""
desired_string = "Ubuntu 22.04.2 LTS"
def localLogingWarning():
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
        file.close()
        print(lines)
        if any(desired_string in line for line in lines):
            with open(fileName, 'a') as file:
                file.write(banner_text)
                print(Fore.GREEN + "\n\033[1m[+] Local Login Warning Banner change SUCCESS: banner changed!" + Style.RESET_ALL)
            file.close()
        else:
            print(Fore.RED + "\n\033[1m[-] Local Login Warning Banner change FAILED: error file seems to be changed" + Style.RESET_ALL)
    else:
        print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error file not found' + Style.RESET_ALL)