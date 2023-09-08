#!/usr/bin/env python3
import os
from colorama import Fore, Style
# Custom Imports
from controls.local_login_warning_banner import localLogingWarning
from controls.telnet_client_not_installed import telnet
from controls.password_creation import passwd_path
from controls.minimumdays import minpass
from controls.http_proxy_server_not_installed import http_proxy

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
    check_os()
    print(Fore.GREEN + possible_commands + Style.RESET_ALL)
    try:
        usrinput()
    except:
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

def check_os():
    os_version = os.popen('lsb_release -ds').read().split()
    if any("Ubuntu 22.04 LTS" in line for line in os_version):
        print(Fore.RED + "\n\033[1m[-] This script can only be run on Ubuntu 22.04 LTS or it's subversions" + Style.RESET_ALL)
        exit()

#Possible command options list
possible_commands = """
[1] Configure the Local Login Waning Banner
[2] Ensure the telnet client is not installed
[3] Ensure password creation requirments are configured
[4] Minimum number of days for password changed
[5] Ensure the HTTP proxy server ( squid server) is not installed
"""

# Command Dictonary to store the commands and related exec nums
command_dict = {
    1: localLogingWarning,
    2: telnet,
    3: passwd_path,
    4: minpass,
    5: http_proxy
}

if __name__ == '__main__':
    if(os.getuid() == 0): # Check if script has sudo privilages
        main()
    else:
        print(Fore.RED + "\n\033[1mThis script has to be run with root privilages\033[0m" + Style.RESET_ALL)