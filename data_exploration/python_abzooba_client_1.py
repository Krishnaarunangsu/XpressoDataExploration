print('Abzooba')
import subprocess

from subprocess import check_output
print(check_output("ls -l", shell=True).decode())
print(check_output("echo $PYTHONPATH", shell=True).decode())
