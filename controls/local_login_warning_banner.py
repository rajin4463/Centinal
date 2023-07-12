import os
import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()
fileName = '/etc/issue'
bashFile = 'scripts/loginMod.sh'
banner_text = """WARNING: Unauthorized access to this system is prohibited. By accessing this system, you agree that your actions may be monitored and recorded. """
bashFileCommand = ["bash", bashFile]
desired_string = "Ubuntu 22.04"
def localLogingWarning():
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
            content = ''.join(lines)
        file.close()
        if (banner_text in content):
            logger.error('''[-] /etc/issue has been modified with the banner.''')
            print(Fore.RED + "\n\033[1m[+] Local Login Warning Banner change FAILED: banner seems to be in place" + Style.RESET_ALL)
        else:
            if any(desired_string in line for line in lines):
                modifyFiles()
            else:
                logger.error('''[-] /etc/issue has been modified.\n [-] OS indication was not found, assuming file has been modified.\n [-] File has not been modified.''')
                print(Fore.RED + "\n\033[1m[-] Local Login Warning Banner change FAILED: error file seems to be changed" + Style.RESET_ALL)
    else:
        logger.error('[-] Local Login Warning Banner change FAILED.\n [-] error `/etc/issue` file not found.')
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
            logger.error('[-] Local Login Warning Banner change FAILED.')
            logger.error(f'{stderr.decode("utf-8")}')
            print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error something went wrong')
            print("\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)
    except(EOFError):
        logger.error('[-] Local Login Warning Banner change FAILED')
        logger.error(f'{EOFError}')
        print(Fore.RED + '\n\033[1m[-] Local Login Warning Banner change FAILED: error something went wrong')
        print("\n\033[1m[-] Check Error logs for more detail." + Style.RESET_ALL)