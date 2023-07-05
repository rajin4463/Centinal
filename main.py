import os
from colorama import Fore, Style
from local_login_warning_banner import localLogingWarning
# Custom Imports

banner = """
 ::::::::  :::::::::: ::::    ::: ::::::::::: ::::::::::: ::::    :::     :::     :::        
:+:    :+: :+:        :+:+:   :+:     :+:         :+:     :+:+:   :+:   :+: :+:   :+:        
+:+        +:+        :+:+:+  +:+     +:+         +:+     :+:+:+  +:+  +:+   +:+  +:+        
+#+        +#++:++#   +#+ +:+ +#+     +#+         +#+     +#+ +:+ +#+ +#++:++#++: +#+        
+#+        +#+        +#+  +#+#+#     +#+         +#+     +#+  +#+#+# +#+     +#+ +#+        
#+#    #+# #+#        #+#   #+#+#     #+#         #+#     #+#   #+#+# #+#     #+# #+#        
 ########  ########## ###    ####     ###     ########### ###    #### ###     ### ########## 
"""

print(Fore.YELLOW + banner + Style.RESET_ALL)
# print(Fore.RED + "[-] This part hasn't still been made, we will make it in time" + Style.RESET_ALL)


def invalidInput():
    print(Fore.RED + "Invalid Input!! Try again" + Style.RESET_ALL)

def main():
    print(Fore.GREEN + "[1] Modify the Local Login Waning Banner" + Style.RESET_ALL)
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