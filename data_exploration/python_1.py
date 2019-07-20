
import subprocess

print('Abzooba')
#subprocess.call(["ls", "-l"])

# p = subprocess.Popen(['docker', 'ps', '|', 'grep', 'myimagename'], stdout=subprocess.PIPE)
#p = subprocess.Popen(['sudo','docker', 'ps'], stdout=subprocess.PIPE)
#print(p.stdout)

subprocess.call(['docker', 'ps'])

