import subprocess

pwd='abz00ba1nc'
cmd='docker ps'

#call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)

cat = subprocess.Popen(['ls', '-l'],
                        stdout=subprocess.PIPE,
                        )

grep = subprocess.Popen(['echo {} | sudo -S {}'.format(pwd, cmd)], shell=True,
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE,
                        )

#cut = subprocess.Popen(['cut', '-f', '3', '-d:'],
                        #stdin=grep.stdout,
                        #stdout=subprocess.PIPE,
                        #)

#end_of_pipe = cut.stdout
end_of_pipe = grep.stdout

print('Output:')
for line in end_of_pipe:
    print('\t', line.strip())
