#!/usr/bin/env python3
import os
from colorama import Fore, Style
# Custom Imports
from local_login_warning_banner import localLogingWarning

banner = """
 ::::::::  :::::::::: ::::    ::: ::::::::::: ::::::::::: ::::    :::     :::     :::        
:+:    :+: :+:        :+:+:   :+:     :+:         :+:     :+:+:   :+:   :+: :+:   :+:        
+:+        +:+        :+:+:+  +:+     +:+         +:+     :+:+:+  +:+  +:+   +:+  +:+        
+#+        +#++:++#   +#+ +:+ +#+     +#+         +#+     +#+ +:+ +#+ +#++:++#++: +#+        
+#+        +#+        +#+  +#+#+#     +#+         +#+     +#+  +#+#+# +#+     +#+ +#+        
#+#    #+# #+#        #+#   #+#+#     #+#         #+#     #+#   #+#+# #+#     #+# #+#        
 ########  ########## ###    ####     ###     ########### ###    #### ###     ### ########## 
"""

print(Fore.BLUE + banner + Style.RESET_ALL)
# print(Fore.RED + "[-] This part hasn't still been made, we will make it in time" + Style.RESET_ALL)


def invalidInput():
    print(Fore.RED + "Invalid Input!! Try again" + Style.RESET_ALL)

possible_commands = """
[1] Modify the Local Login Waning Banner
"""

def main():
    print(Fore.GREEN + possible_commands + Style.RESET_ALL)
    command_dict = {
        1: localLogingWarning
    }
    exit_flag = True

    while exit_flag:
        user_input = int(input("Enter command number to run. Input -1 to exit\n"))
        if user_input == -1:
            print(Fore.GREEN + "[-] Bye Bye " + Style.RESET_ALL + "👋")
            exit_flag = False
        else:
            command_functions = command_dict.get(user_input, invalidInput)
            command_functions()


if(os.getuid() == 0):
    main()
else:
    print(Fore.RED + "This script has to be run with root privilages" + Style.RESET_ALL)