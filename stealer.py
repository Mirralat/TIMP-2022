from base64 import encode
import subprocess
import hashlib
from sys import stdout


def steal():
    name = subprocess.run('whoami', shell=True)
    computer = subprocess.run('hostname', shell=True)
    proc = subprocess.run("grep -c 'model name' /proc/cpuinfo", shell=True, capture_output=True)
    processor = proc.stdout.decode('UTF-8').rstrip()
    mem = subprocess.run("grep MemTotal /proc/meminfo", shell=True, capture_output=True)
    memory = mem.stdout.decode('UTF-8').rstrip()
    memory = memory.replace(" ", "").replace("MemTotal:", "")
    data = [str(name.args), str(computer.args), str(processor), str(memory)]
    encrypted = []

    for dat in data:
        result = hashlib.md5(dat.encode()).hexdigest()
        encrypted.append(result)

    with open('sys.tat', 'w') as f:
        for line in encrypted:
            f.write(line)
            f.write('\n')

steal()

