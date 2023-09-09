# import fileinput

# # Define the file path
# file_path = '/etc/pam.d/common-password'

# # Define the new 'remember' value
# new_remember_value = 5

# # Flag to track whether the line was modified
# line_modified = False

# # Loop through the file using fileinput
# for line in fileinput.input(file_path, inplace=True):
#     parts = line.split()
#     if line.startswith('password [success=1 default=ignore] pam_unix.so obscure use_authtok try_first_pass yescrypt'):
#         for i, part in enumerate(parts):
#             if part.startswith('remember='):
#                 current_remember = int(part.split('=')[1])
#                 if current_remember < new_remember_value:
#                     parts[i] = f'remember={new_remember_value}'
#                     line_modified = True
#                     break
#     else:
#         # If 'remember' option is not found, add it
#         parts.insert(-1, f'remember={new_remember_value}')
#         line_modified = True

#     print(' '.join(parts), end='')

# if line_modified:
#     print(f"\nUpdated '{file_path}' with the new 'remember' value: {new_remember_value}")
# else:
#     print(f"'remember' value in '{file_path}' is already set to {new_remember_value}")

import os
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()
fileName = '/etc/pam.d/common-password'

file_path = '/etc/pam.d/common-password'
name_to_find ='pam_unix.so'
new_line_content = 'password        [success=1 default=ignore]      pam_unix.so obscure use_authtok try_first_pass yescrypt remember=5'


def passwd_path():
    if os.path.exists(fileName):
        with open(fileName,'r') as file:
            lines = file.readlines()
            content = ''.join(lines)
        file.close()
        if(new_line_content in content):
            print(Fore.GREEN + '\n\033[1m[+] Password resue limit Already updated!' + Style.RESET_ALL)
        else:
            userCheck = input(Fore.GREEN + f"\n\033[1m[+] Do you want to change Password resue limit to 5 [Y/n] ? " + Style.RESET_ALL)
            userCheck = userCheck.lower()
            if userCheck == 'y':
                modifypass(file_path, name_to_find,new_line_content)
            elif (userCheck == 'n'): 
                print(Fore.RED + "\n\033[1m[+] Password resue limit won't be chnaged!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "\n\033[1m[-] INVALID INPUT: Enter 'y' or 'n'.\n" + Style.RESET_ALL)
                passwd_path()
    else:
        logger.error("[-] Password resue limit FAILED: File not found")
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
                        print(Fore.GREEN + '\n\033[1m[+] Password resue limit set to remember 5 old passwrods!' + Style.RESET_ALL)
                    else:
                        temp_file.write(line_content)
            os.replace(temp_file_path, file_path)
            return True
        else:
            logger.error(f"[-] Password resue limit FAILED: {fileName} File not found")
            logger.error("[-] Password resue limit not set.")
            print(Fore.RED + f"\n\033[1m[-] Password resue limit FAILED: {fileName} File not found" + Style.RESET_ALL)
            print(Fore.RED + "\n\033[1m[-] Password resue limit not set." + Style.RESET_ALL)