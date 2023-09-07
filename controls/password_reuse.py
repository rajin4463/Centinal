import os
import misc.logger
from colorama import Fore, Style
logger = misc.logger.setup_logger()

file_name = '/etc/pam.d/common-password'
remember_option = '5'

def passwd_reuse():
  with open(file_name, 'r') as f:
    lines = f.readlines()

  for i, line in enumerate(lines):
    if line.startswith('password required pam_pwcheck.so'):
      lines[i] = 'password required pam_pwcheck.so nullok remember=' + remember_option

  with open(file_name, 'w') as f:
    f.writelines(lines)
