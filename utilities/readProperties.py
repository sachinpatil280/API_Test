import configparser
import yaml

class ReadConfig:

    @staticmethod
    def readConfig_iniFile(config_section):
        """
        :param config_section: section in config.ini file from where to read data.
        :return: values read from config.ini file
        """
        config = configparser.RawConfigParser()
        config.read("..\\resources\\config.ini")
        values = dict(config.items(config_section))
        return values

    @staticmethod
    def readConfig_yamlFile(config_section):
        """
        :param config_section: section in config.yaml file from where to read data.
        :return: values read from config.yaml file
        """
        path = "../resources/config.yaml"
        with open(path) as c:
            config = yaml.load(c, Loader=yaml.FullLoader)
        return config[config_section]