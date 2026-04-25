import re

class InputValidator:
    def __init__(self, username_pattern: str = r'^[a-zA-Z0-9_]{3,20}$', age_range: tuple = (0, 120)):
        self.username_pattern = username_pattern
        self.age_range = age_range

    def validate_username(self, username: str) -> bool:
        if re.match(self.username_pattern, username):
            return True
        raise ValueError(f'Invalid username: {username}')

    def validate_age(self, age: int) -> bool:
        if self.age_range[0] <= age <= self.age_range[1]:
            return True
        raise ValueError(f'Invalid age: {age}')

    def validate_input(self, username: str, age: int):
        try:
            self.validate_username(username)
            self.validate_age(age)
            return True
        except ValueError as e:
            print(f'Validation error: {e}')
            return False

if __name__ == '__main__':
    validator = InputValidator()
    user_data = [('ValidUser01', 25), ('!nv4lidUser', 130)]
    for username, age in user_data:
        if validator.validate_input(username, age):
            print(f'{username}, {age} is valid')
        else:
            print(f'{username}, {age} is invalid')
