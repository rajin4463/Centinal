import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()

def http_proxy(): 
    compare = "squid	install ok installed	installed"
    command = "dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' squid"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')

    if compare in output:
        print(Fore.GREEN + "\n\033[1m[+] http proxy server (squid server) was found." + Style.RESET_ALL)
        user_input = input(Fore.GREEN + "\n\033[1m[+] Do you want to remove http proxy server? (y/n): " + Style.RESET_ALL)
        if user_input.lower() not in ['y', 'n']:
            print(Fore.RED + "\n\033[1m[-] Invalid input. Please enter 'y' or 'n'." + Style.RESET_ALL)
            http_proxy()
        elif user_input.lower() == 'n':
            return
        else:   
            print(Fore.RED + "\n\033[1m[-] Purging http server" + Style.RESET_ALL)
            purgeCommand = ["apt-get", "purge", "-y", "squid"]
            process = subprocess.run(purgeCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if process.returncode == 0:
                print(Fore.GREEN + "\n\033[1m[+] Successfully purged http proxy server." + Style.RESET_ALL)
            else:
                logger.error("[-] http proxy server purge FAILED.\n")
                logger.error(f'[-] {process.stderr.decode("utf-8")}')
                print(Fore.RED + "\n\033[1m[-] http proxy server purge FAILED: error something went wrong.\n")
                print("\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n\033[1m[-] http proxy server purge FAILED: error http proxy server dosen't seem to be installed." + Style.RESET_ALL)
        logger.error(f"[-] http proxy server purge FAILED\n [-] {output}")