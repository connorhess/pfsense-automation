from paramiko import SSHClient
from pfsense.scp import SCPClient
from pfsense import config
# import xmltodict
import pprint
from ast import literal_eval
# from dict2xml import dict2xml
import xml.etree.ElementTree as ET

# config = configparser.ConfigParser()
# config.read('../Config.ini')

print("Core.py")
pfsense_config_path = config['DEFAULT']['pfsense_config_path']
pfsense_config_name = config['DEFAULT']['pfsense_config_name']
pfsense_full_path = f"{pfsense_config_path}/{pfsense_config_name}"


def run():
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


    tree = ET.parse(pfsense_config_name)
    root = tree.getroot()

    for i in range(2):
        for L1 in root:
            if L1.tag == 'captiveportal':

                for Parent in L1:
                    if Parent.tag == 'cpbhswifi':

                        for child in Parent:
                            if child.tag == 'passthrumac':
                                # print("child", child)

                                for item in child:
                                    if item.tag == 'mac':

                                        item_mac = (item.text)
                                        # print(item_mac)
                                        if item_mac not in keep_mac_list:
                                            Parent.remove(child)
                        # print(item_mac)


    tree.write(pfsense_config_name)



    print("Edited File")
    scp.put(pfsense_config_name, pfsense_full_path)
    print("Wrote File")



    # Uploading the 'test' directory with its content in the
    # '/home/user/dump' remote directory

    # scp.put('test', recursive=True, remote_path='/home/user/dump')

    scp.close()
