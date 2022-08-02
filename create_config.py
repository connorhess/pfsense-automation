import configparser


config = configparser.ConfigParser()
config.read('Config.ini')
# print(config['DEFAULT']['path'])     # -> "/path/name/"

# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

server_address = input("Server Address ['example.com']: ")
# server_address = "192.168.1.2"
config['DEFAULT']['server_address'] = server_address


# server_address = input("Server Address: ['example.com']")





















with open('config.ini', 'w') as configfile:    # save
    config.write(configfile)
