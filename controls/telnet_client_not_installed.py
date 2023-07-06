import subprocess

def telnet():
    command = "dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' telnet"
    process=subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout
    compare = "telnet	install ok installed	installed"
    
    if compare in output:
        print("Desired string found in the command output!")
    else:
        print("Desired string not found in the command output.")