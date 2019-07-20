print('Abzooba')
from subprocess import check_output



print(check_output("ls -l", shell=True).decode())
#print(check_output("echo $PYTHONPATH", shell=True).decode())
pwd='abz00ba1nc'
cmd='docker ps'
print(check_output("echo {} | sudo -S {}".format(pwd, cmd), shell=True).decode())



