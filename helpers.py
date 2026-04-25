import os
import json
import random

class RobloxHelper:
    @staticmethod
    def load_json(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_json(data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def generate_random_id():
        return random.randint(100000, 999999)

    @staticmethod
    def format_username(username):
        return username.strip().lower()

    @staticmethod
    def is_valid_username(username):
        return 3 <= len(username) <= 20 and username.isalnum()