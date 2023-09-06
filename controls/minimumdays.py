import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()


def getInput():
    username = input(
        Fore.GREEN + "\n\033[1m[+] Enter the user name to be changed: " + Style.RESET_ALL)
    min_days = input(
        Fore.GREEN + "\n\033[1m[+] Enter a minimum number of days for the password to be changed: " + Style.RESET_ALL)
    return username, min_days


def minpass():
    username, min_days = getInput()
    check_command = ["chage", "-l", username]
    check_process = subprocess.run(check_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    if check_process.returncode != 0:
        logger.error("[-] Minimum number of days for password change FAILED: Failed to run chage command.\n")
        logger.error(f'[-] {check_command.stderr.decode("utf-8")}')
        print(Fore.RED + "\n\033[1m[-] Minimum number of days for password change FAILED: error something went wrong.\n")
        print("\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)
        return
    else:
        set_min_days = int(check_proces.stdout.split()[27])
        print(
            Fore.GREEN + f"\n\033[1m[+] Current minimum number of days for password change is: {set_min_days}" + Style.RESET_ALL)
        userCheck = input(
            Fore.GREEN + f"\n\033[1m[+] Do you want to change this [Y/n] ? " + Style.RESET_ALL)
        userCheck = userCheck.lower()
        if userCheck == 'y':
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
        elif (userCheck == 'n'):
            return
        else:
            print(Fore.RED + "\n\033[1m[-] INVALID INPUT: Enter 'y' or 'n'.\n" + Style.RESET_ALL)
            minpass()