import configparser


config = configparser.ConfigParser()
config.read('../Config.ini')
print(config['DEFAULT']['server_address'])     # -> "/path/name/"
