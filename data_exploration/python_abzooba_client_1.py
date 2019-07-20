print('Xpresso AI-Abzooba')
print('***************************************')
from subprocess import check_output



#print(check_output("ls -l", shell=True).decode())
#print(check_output("echo $PYTHONPATH", shell=True).decode())
print('Docker Installation Check')
print('***************************************')
pwd='abz00ba1nc'
cmd='docker ps'
print(check_output("echo {} | sudo -S {}".format(pwd, cmd), shell=True).decode())

print('Kubernetes Installation Check')
print('***************************************')
cmd_1 = 'kubectl get services'
#print(check_output("kubectl explain pods,svc",shell=True).decode())
print(check_output("echo {} | sudo -S {}".format(pwd, cmd_1), shell=True).decode())
print('*****************************************************************************')

print('Kubeflow Installation Check')
print('***************************************')
cmd_2 ='kubectl -n kubeflow get  all'
print(check_output("echo {} | sudo -S {}".format(pwd, cmd_2), shell=True).decode())
print('*****************************************************************************')

print('Python3 Installation Check')
print('***************************************')
cmd_3 ='python3 --version'
print(check_output("echo {} | sudo -S {}".format(pwd, cmd_3), shell=True).decode())
print('*****************************************************************************')

print('Git Installation Check')
print('***************************************')
cmd_4 ='git status'
print(check_output("echo {} | sudo -S {}".format(pwd, cmd_4), shell=True).decode())
print('*****************************************************************************')


