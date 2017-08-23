import os
import psutil
import subprocess
from multiprocessing import Process
import random

def rscript_run(cmd):
    curr_process = Process(target=subprocess.Popen, args=(cmd,),
                           kwargs={"shell": True, "universal_newlines": True})
    curr_process.start()
    parent = psutil.Process(os.getpid())
    return parent.children(recursive=True)

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
        port = random.randint(1000, 9999)
    cmd = f"Rscript {path} {port}"
    pid = rscript_run(cmd)
    print('I reached this')
    print(f'pid: {d for d in pid}, port: {port}')
    #QUESTION: how do you terminate the process
