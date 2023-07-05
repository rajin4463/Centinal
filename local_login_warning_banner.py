import os
import re
from colorama import Fore, Style
fileName = 'etc/issue'
banner_text = """WARNING: Unauthorized access to this system is prohibited.
By accessing this system, you agree that your actions may be monitored and recorded.
"""
def localLogingWarning():
    if os.path.exists(fileName):
        with open(fileName, 'w') as file:
            file.write(banner_text)
            print(Fore.GREEN + "[+] Local Login Warning Banner change SUCCESS: banner changed!" + Style.RESET_ALL)
    else:
        print(Fore.RED + '[-] Local Login Warning Banner change FAILED: error file not found' + Style.RESET_ALL)