import subprocess

def telnet():
    command = ["dpkg-query", "-W", "-f='${binary:Package}\t${Status}\t${db:Status-Status}\n'", "telnet"]
    process=subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout
    print(output)