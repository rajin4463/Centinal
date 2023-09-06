import shlex
import subprocess
# import misc.logger
from colorama import Fore, Style
# logger = misc.logger.setup_logger()

# commands = "grep PASS_MIN_DAYS /etc/login.defs"
# execute_result = subprocess.run(shlex.split(commands), text=True, capture_output=True)

def set_min_days_between_password_changes(username, min_days):
    try:
        chage_command = ["chage", "-m", str(min_days), username]
        subprocess.run(chage_command)
        print("Value replaced successfully.")
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def getInput():
    COMPANY_POLICY_DAY = input(Fore.GREEN + f"\n\033[1m[+] Enter the user name to be changed: " + Style.RESET_ALL)
    min_days = input("[+] Enter a minimum number of days for the password to be changed: " + Style.RESET_ALL)

def minimum():
    if (int(min_days) >= 1):
        set_min = set_min_days_between_password_changes(COMPANY_POLICY_DAY, min_days)
        if (set_min == True):
            print(Fore.GREEN + f"\n\033[1m[+] Minimum day between Passwords have been set" + Style.RESET_ALL) 
        else:
            print(Style.RED + "\n\033[1m[-] Error Occurred, check logs for more information" + Style.RESET_ALL)
            # logger.error('''[-] Error Occurred, while changing the minimum number of days for the password''')
            # logger.error(e)

        
    else:
        print(Fore.RED + f"\n\033[1m[-] Minimum day's must be greater than or equal to 1" + Style.RESET_ALL) 
        getInput()

COMPANY_POLICY_DAY = input(Fore.GREEN + f"\n\033[1m[+] Enter the user name to be changed: " + Style.RESET_ALL)
min_days = input(Fore.GREEN + "\n\033[1m[+] Enter a minimum number of days for the password to be changed: " + Style.RESET_ALL)
minimum()