import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()

# commands = "grep PASS_MIN_DAYS /etc/login.defs"
# execute_result = subprocess.run(shlex.split(commands), text=True, capture_output=True)

def getInput():
    username = input(Fore.GREEN + "\n\033[1m[+] Enter the user name to be changed: " + Style.RESET_ALL)    
    min_days = input(Fore.GREEN + "\n\033[1m[+] Enter a minimum number of days for the password to be changed: " + Style.RESET_ALL)
    return username, min_days

def minpass():
    username ,min_days = getInput()
    if (int(min_days) >= 1):
        chage_command = ["chage", "-m", str(min_days), username]
        process = subprocess.run(chage_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode == 0:
            print(Fore.GREEN + "\n\033[1m[+] Successfully Changed minimum number of days for password change" + Style.RESET_ALL)
        else:
            logger.error("[-] Minimum number of days for password change FAILED.\n")
            logger.error(f'[-] {process.stderr.decode("utf-8")}')
            print(Fore.RED + "\n\033[1m[-] Minimum number of days for password change FAILED: error something went wrong.\n")
            print("\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n\033[1m[-] Minimum number of days should be lager than 1" + Style.RESET_ALL)
        minpass()

def checkConfig():
    commands = ["grep", "PASS_MIN_DAYS", "/etc/login.defs"]
    execute_result = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(execute_result.stdout)