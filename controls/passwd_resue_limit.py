import fileinput

# Define the file path
file_path = '/etc/pam.d/common-password'

# Define the new 'remember' value
new_remember_value = 5

# Flag to track whether the line was modified
line_modified = False

# Loop through the file using fileinput
for line in fileinput.input(file_path, inplace=True):
    parts = line.split()
    if line.startswith('password [success=1 default=ignore] pam_unix.so obscure use_authtok try_first_pass yescrypt'):
        for i, part in enumerate(parts):
            if part.startswith('remember='):
                current_remember = int(part.split('=')[1])
                if current_remember < new_remember_value:
                    parts[i] = f'remember={new_remember_value}'
                    line_modified = True
                    break
        else:
            # If 'remember' option is not found, add it
            parts.insert(-1, f'remember={new_remember_value}')
            line_modified = True

    print(' '.join(parts), end='')

if line_modified:
    print(f"\nUpdated '{file_path}' with the new 'remember' value: {new_remember_value}")
else:
    print(f"'remember' value in '{file_path}' is already set to {new_remember_value}")
