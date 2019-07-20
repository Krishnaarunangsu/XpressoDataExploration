
from  subprocess import call

print('Abzooba')
#subprocess.call(["ls", "-l"])

# p = subprocess.Popen(['docker', 'ps', '|', 'grep', 'myimagename'], stdout=subprocess.PIPE)
#p = subprocess.Popen(['sudo','docker', 'ps'], stdout=subprocess.PIPE)
#print(p.stdout)

# subprocess.call(['docker', 'ps'])
pwd='abz00ba1nc'
cmd='docker ps'

call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)

