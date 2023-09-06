import shlex
import subprocess

commands = "grep PASS_MIN_DAYS /etc/login.defs"
execute_result = subprocess.run(shlex.split(commands), text=True, capture_output=True)
print(execute_result.stdout.split("\n"))

if "/etc/login.defs:PASS_MIN_DAYS\t0" in execute_result.stdout:
    print(True)
else:
    print(False)

COMPANY_POLICY_DAY = input("Enter a minimum number of days for the password to be changed: ")

def replace_in_login_defs(user_input):
    old_string = 'PASS_MIN_DAYS\t0'
    new_string = f'PASS_MIN_DAYS\t{user_input}'
    try:
        with open('/etc/login.defs', 'r') as file:
            content = file.read()
            content = content.replace(old_string, new_string)
        with open('/etc/login.defs', 'w') as file:
            file.write(content)
        print("Value replaced successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

replace_in_login_defs(COMPANY_POLICY_DAY)
