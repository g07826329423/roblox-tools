import json
import os

DEFAULT_CONFIG = {
    "api_key": "YOUR_API_KEY",
    "timeout": 30,
    "retry_attempts": 3,
    "debug": false
}

class ConfigLoader:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

# Usage example:
if __name__ == '__main__':
    config = ConfigLoader()
    print(config.get('api_key'))
    print(config.get('timeout'))