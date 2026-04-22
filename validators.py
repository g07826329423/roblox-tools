import re
from typing import Any, Dict

def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_valid_username(username: str) -> bool:
    return bool(re.match('^[a-zA-Z0-9]{3,20}$', username))


def is_positive_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and value > 0


def is_valid_email(email: str) -> bool:
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))


def validate_user_data(user_data: Dict[str, Any]) -> bool:
    return (is_non_empty_string(user_data.get('username')) and 
            is_valid_username(user_data['username']) and 
            is_non_empty_string(user_data.get('email')) and 
            is_valid_email(user_data['email']) and 
            is_positive_number(user_data.get('age', 0)))


def validate_item_data(item_data: Dict[str, Any]) -> bool:
    return (is_non_empty_string(item_data.get('name')) and 
            is_positive_number(item_data.get('price', 0)))