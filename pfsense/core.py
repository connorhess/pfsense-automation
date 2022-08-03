from paramiko import SSHClient
from pfsense.scp import SCPClient
from pfsense import config
import xmltodict
import pprint
from ast import literal_eval
from dict2xml import dict2xml


# config = configparser.ConfigParser()
# config.read('../Config.ini')

print("Core.py")
pfsense_config_path = config['DEFAULT']['pfsense_config_path']
pfsense_config_name = config['DEFAULT']['pfsense_config_name']
pfsense_full_path = f"{pfsense_config_path}/{pfsense_config_name}"


ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(config['DEFAULT']['server_address'], username=config['DEFAULT']['username'], password=config['DEFAULT']['password'])

stdin, stdout, stderr = ssh.exec_command('8')


cmd_output = stdout.read()
print('log printing: ', cmd_output)
# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())


scp.get(pfsense_full_path)
print("Read File")
try:
    keep_mac_list = literal_eval(config['DEFAULT']['exclude_mac'])
except:
    print("Error in exclude mac list in config file")
    keep_mac_list = []

new_passthrough_mac = []
with open(pfsense_config_name, 'r') as f:
    xml = (f.read())
    my_dict = xmltodict.parse(xml)
    passthrough_mac = my_dict['pfsense']['captiveportal']['cpbhswifi']['passthrumac']

for item in passthrough_mac:
    if item['mac'] in keep_mac_list:
        new_passthrough_mac.append(item)

# pprint.pprint(new_passthrough_mac)
my_dict['pfsense']['captiveportal']['cpbhswifi']['passthrumac'] = new_passthrough_mac

# pprint.pprint(my_dict['pfsense']['captiveportal']['cpbhswifi']['passthrumac'])

new_xml = dict2xml(my_dict)
print(new_xml)

with open(pfsense_config_name, 'w') as f:
    f.write(new_xml)

print("Edited File")
scp.put(pfsense_config_name, pfsense_full_path)
print("Wrote File")



# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory

# scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()
