import subprocess

def telnet():
    command = "dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' telnet"
    # process=subprocess.check_output(command, shell=True, stdout=subprocess.PIPE)
    print(command)