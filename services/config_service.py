import yaml

class Config:
    
    config: any = {}
    
    def init(config_file='config/config.yaml'):
        with open(config_file, 'r') as file:
            Config.config = yaml.safe_load(file)

    def get_app_config():
        return Config.config.get('app', {})