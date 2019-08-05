import subprocess

p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE, shell=True)

print(p.communicate())
