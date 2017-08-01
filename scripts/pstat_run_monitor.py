import subprocess
from multiprocessing import Process
import random

def rscript_run(cmd):
    Process.run(cmd, shell=True, universal_newlines=True)
    for outline in iter(process_out.stdout.readline, ""):
        yield outline
    process_out.stdout.close()
    return_code = process_out.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def get_open_ports():
    cmd = 'netstat -vatn | grep -i "127.0.0.1" | awk "{print $4}"'
    output = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    result, err = output.communicate()
    return list(map(lambda x: x.split(':')[-1], result))

if __name__ == '__main__':
    path = "pstat_rscript.R"
    open_ports = get_open_ports()
    port = open_ports[0]
    while port in open_ports:
        port = random.randint(0, 9999)
    print(port)
    cmd = f"Rscript {path} {port}"
    for line in rscript_run(cmd):
        pass
    #QUESTION: how do you terminate the process
