#!/usr/bin/env python3
import os
import threading
from colorama import Fore, Style
# Custom Imports
from controls.local_login_warning_banner import localLogingWarning
from controls.telnet_client_not_installed import telnet

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

def main():
    print(Fore.GREEN + possible_commands + Style.RESET_ALL)
    try:
        usrinput()
    except(EOFError):
        print(EOFError)
        typeError()
        main()


def usrinput():
    exit_flag = True
    while exit_flag:
        user_input = int(input("\n\033[1mEnter command number to run. Input -1 to exit\033[0m\n"))
        if user_input == -1:
            print(Fore.GREEN + "[-] Bye Bye " + Style.RESET_ALL + "👋")
            exit_flag = False
        else:
            command_functions = command_dict.get(user_input, invalidInput)
            command_functions()

def invalidInput():
    print(Fore.RED + "[-] Invalid Input!! Try again." + Style.RESET_ALL)
    print(Fore.GREEN + possible_commands + Style.RESET_ALL)

def typeError():
    print(Fore.RED + "[-] Invalid Input Type!! Only numbers are allowed. Try again." + Style.RESET_ALL)

def runAll():
    #multithreading
    local_Warning_Banner = threading.Thread(target=local_Loging_Warning, daemon=False)
    telnet_client_removal = threading.Thread(target=telnet, daemon=False)

    local_Warning_Banner.start()
    telnet.start()

    #wait until threads finish excuting before running anything after <POINT>
    local_Warning_Banner.join()
    telnet.join()

    """
    <POINT>
    anything below this line will only run after the above threads have executed"""
        

#Possible command options list
possible_commands = """
[1] Configure the Local Login Waning Banner
[2] Ensure the telnet client is not installed
[6] Run fix for all controls
"""

# Command Dictonary to store the commands and related exec nums
command_dict = {
    1: localLogingWarning,
    2: telnet,
    6: runAll
}

if __name__ == '__main__':
    if(os.getuid() == 0):
        main()
    else:
        print(Fore.RED + "\n\033[1mThis script has to be run with root privilages\033[0m" + Style.RESET_ALL)