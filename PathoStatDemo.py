import subprocess

command = 'Rscript'
path2script = 'C:\\Users\\hjfan\\Documents\\R Scripts\\PathoStatDemo.R'

cmd = [command, path2script]

x = subprocess.check_output(cmd, universal_newlines=True)
