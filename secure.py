import subprocess

subprocess.run(f'sudo chmod 000 sys.tat', shell=True)
subprocess.run(f'sudo chattr +i sys.tat', shell=True, check=True)
