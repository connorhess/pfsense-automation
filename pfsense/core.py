from paramiko import SSHClient
from pfsense.scp import SCPClient
from pfsense import config

# config = configparser.ConfigParser()
# config.read('../Config.ini')

print("Core.py")

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(config['DEFAULT']['server_address'])

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory

# scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()
