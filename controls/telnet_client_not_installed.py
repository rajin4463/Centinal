import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()

def telnet():
    compare = "telnet	install ok installed	installed"
    command = "dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' telnet"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')

    if compare in output:
        print(Fore.RED + "\n\033[1m[+] Telnet client was found.")
        user_input = input(Fore.GREEN + "\n\033[1m[+] Do you want to remove Telnet client? [Y/n]: " + Style.RESET_ALL)
        if user_input.lower() not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            telnet()
        elif user_input.lower() == 'n':
            return
        else:
            print("\n\033[1m[-] Purging client" + Style.RESET_ALL)
            purgeCommand = ["apt-get", "purge", "-y", "telnet"]
            process = subprocess.run(purgeCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if process.returncode == 0:
                print(Fore.GREEN + "\n\033[1m[+] Successfully purged Telnet Client." + Style.RESET_ALL)
            else:
                logger.error("[-] Telnet client purge FAILED.\n")
                logger.error(f'[-] {process.stderr.decode("utf-8")}')
                print(Fore.RED + "\n\033[1m[-] Telnet client purge FAILED: error something went wrong.\n")
                print("\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n\033[1m[-] Telnet client purge FAILED: error telnet client dosen't seem to be installed." + Style.RESET_ALL)
        logger.error(f"[-] Telnet client purge FAILED\n")
        logger.error(f'[-] {process.stderr.decode("utf-8")}')