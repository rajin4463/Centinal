import os
import subprocess
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()
fileName= '/etc/pam.d/common-password'

pass_string = 'password        requisite                       pam_pwquality.so minlen=14 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=7 enforce_for_root retry=3'

file_path = '/etc/pam.d/common-password'
name_to_find ='pam_pwquality.so'
new_line_content = 'password        requisite                       pam_pwquality.so minlen=14 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=7 enforce_for_root retry=3'


def passwd_path():
    if os.path.exists(fileName):
        with open(fileName,'r') as file:
            lines = file.readlines()
            content = ''.join(lines)
        file.close()
        if(pass_string in content):
            print(Fore.GREEN + '\n\033[1m[+] Already updated!' + Style.RESET_ALL)
        else:
            
            modifypass(file_path, name_to_find,new_line_content)

    else:
        logger.error("[-] Minimum password length FAILED: File not found")
        logger.error(f"Common password path doesn't exists. \n File not found: {fileName}")
        print(Fore.RED + "\n\033[1m[-] Common password path doesn't exists" + Style.RESET_ALL)
        print(Fore.RED + "\n\033[1mCheck logs for more information" + Style.RESET_ALL)

def find_line_number_by_name(file_path ,name_to_find):
    with open(file_path, 'r') as input_file:
        for line_number, line_content in enumerate(input_file,start=1):
            if name_to_find in line_content:
                return line_number
    return None

def modifypass(file_path, name_to_find,new_line_content):
        line_number_to_edit = find_line_number_by_name(file_path, name_to_find)
        if line_number_to_edit is not None:
            temp_file_path = file_path + '.tmp'
            with open(file_path,'r') as input_file, open(temp_file_path, 'w') as temp_file:
                for line_number, line_content in enumerate(input_file, start=1):
                    if line_number == line_number_to_edit:
                        temp_file.write(new_line_content + '\n')
                        print(Fore.GREEN + '\n\033[1m[+] Minimum password length set to 14 characters!' + Style.RESET_ALL)
                    else:
                        temp_file.write(line_content)
            os.replace(temp_file_path, file_path)
            return True
        else:
            logger.error("[-] Minimum password length FAILED: pam_pwquality.so File not found")
            logger.error("[-] Minimum password length not set.")
            print(Fore.RED + "\n\033[1m[-] Minimum password length FAILED: pam_pwquality.so File not found" + Style.RESET_ALL)
            print(Fore.RED + "\n\033[1m[-] Minimum password length not set." + Style.RESET_ALL)