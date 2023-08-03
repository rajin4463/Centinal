import os
import subprocess
from colorama import Fore, Style
#fileName= '/etc/pam.d/common-password'
fileName= '/home/janith/hello'

pass_string = 'password        requisite                       pam_pwquality.so minlen=14 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=7 enforce_for_root retry=3'

file_path = '/home/janith/hello'
name_to_find ='pam_pwquality.so'
new_line_content = 'password        requisite                       pam_pwquality.so minlen=14 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=7 enforce_for_root retry=3'


def passwd_path():
    if os.path.exists(fileName):
        with open(fileName,'r') as file:
            lines = file.readlines()
            content = ''.join(lines)
        file.close()
        if(pass_string in content):
            print(Fore.RED + "\n\033[1m[+] Already updated]" + Style.RESET_ALL)
        else:
            
            modifypass(file_path, name_to_find,new_line_content)

    else:
        print(Fore.RED + "\n\033[1m[-] Common password path doesn't exists")

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
                        print(Fore.RED + "\n\033[1m[-] A")
                    else:
                        temp_file.write(line_content)
                        print(Fore.RED + "\n\033[1m[-] B")
            os.replace(temp_file_path, file_path)
            return True
        else:
            print(Fore.RED + "\n\033[1m[-] pam_pwquality.so file not found. Trying to installing")
            install_pam_pwquality_package()
            print(Fore.RED + "\n\033[1m[-] pam_pwquality.so file installed successfully. Please rerun the script!")
            #return False

def install_pam_pwquality_package():
    try:
        subprocess.run(["sudo", "apt-get","install", "-y", "libpam-pwquality"])
        return True
    except Exception as e:
        print(Fore.RED + "\n\033[1m[-] Failed to install libpam-pwquality")
        return False
            