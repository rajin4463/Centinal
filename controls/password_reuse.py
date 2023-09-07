import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()

file_name = '/etc/pam.d/common-password'
remember_option = '5'

def passwd_reuse():
    # Configure password history in common-auth file
    reuse_command = ['sed', '-i', f'$ a\password required pam_pwhistory.so remember={remember_option}', '/etc/pam.d/common-auth']
    rem_rum = subprocess.run(reuse_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if rem_rum.returncode == 0:
        print(Fore.GREEN + f"\n\033[1m[+] Password reuse limit set!" + Style.RESET_ALL)
    else:
        logger.error("[-] Password reuse limit set FAILED: Failed to set Password reuse limit.\n")
        logger.error(f'[-] {check_command.stderr.decode("utf-8")}')
        print(Fore.RED + "\n\033[1m[-] Password reuse limit set FAILED: Failed to set Password reuse limit." + Style.RESET_ALL)
        print(Fore.RED + "\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)