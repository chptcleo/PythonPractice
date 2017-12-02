import paramiko

host = '192.168.1.106'
user = 'root'
password = '3035188'
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=host, username=user, password=password)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()