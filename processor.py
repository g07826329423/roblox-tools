import json
import re

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'username' not in data or not isinstance(data['username'], str):
        raise ValueError('Username is required and must be a string')
    if 'age' in data:
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise ValueError('Age must be a non-negative integer')
    return True

def process_data(data):
    validate_input(data)
    # Assuming further processing here
    return json.dumps({'status': 'success', 'data': data})

if __name__ == '__main__':
    raw_input = '{"username": "player1", "age": 10}'
    data = json.loads(raw_input)
    try:
        result = process_data(data)
        print(result)
    except ValueError as e:
        print(f'Error: {e}')