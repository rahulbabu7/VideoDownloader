import subprocess


sudo_password = ''

command = 'paru'

subprocess.run(f'echo {sudo_password} | sudo -S {command}', shell=True)
