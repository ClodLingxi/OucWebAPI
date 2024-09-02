import configparser

class ConfigOfTest:

    def __init__(self, config_path):
        self._config = configparser.ConfigParser()
        self._config.read(config_path)

        self._username = self._config.get('login', 'username')
        self._password = self._config.get('login', 'password')

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password