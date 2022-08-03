import configparser


config = configparser.ConfigParser()
config.read('Config.ini')
# print(config['DEFAULT']['path'])     # -> "/path/name/"

# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

server_address = input("Server Address ['example.com']: ")
# server_address = "192.168.1.2"
config['DEFAULT']['server_address'] = server_address

username = input("Username ['root']: ")
# server_address = "192.168.1.2"
config['DEFAULT']['username'] = username

password = input("Password ['test1234']: ")
# server_address = "192.168.1.2"
config['DEFAULT']['password'] = password

pfsense_config_path = input("Config File Full Path ['/dir' without config.php]: ")
# server_address = "192.168.1.2"
config['DEFAULT']['pfsense_config_path'] = pfsense_config_path


pfsense_config_name = input("Config File Name ['config.php']: ")
# server_address = "192.168.1.2"
config['DEFAULT']['pfsense_config_name'] = pfsense_config_name


# server_address = input("Server Address: ['example.com']")





















with open('config.ini', 'w') as configfile:    # save
    config.write(configfile)
