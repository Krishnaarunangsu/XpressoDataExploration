print('Abzooba')
import subprocess

from subprocess import check_output
print(check_output("dir C:", shell=True).decode())
print(check_output("echo %PYTHONPATH%", shell=True).decode())
