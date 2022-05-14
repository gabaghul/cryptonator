from envyaml import EnvYAML

env = EnvYAML('config.yml', strict=False)


MONGO_URI = env['mongo']['uri']
MONGO_PORT = env['mongo']['port']