import yaml
import pymongo

MONGO_URI = ""
MONGO_PORT = 0

with open(r'../config.yml') as file:
    file = yaml.load(file, Loader=yaml.FullLoader)
    mongo_conf = file['mongo']
    MONGO_URI = mongo_conf['uri']
    MONGO_PORT = mongo_conf['port']