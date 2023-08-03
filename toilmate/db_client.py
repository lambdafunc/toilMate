import json
import os

# Update JSON_FILE_PATH if needed
JSON_FILE_PATH = "toil_balance.json"


def get_toil_balance(user_id):
    """Get the TOIL balance for a user."""
    all_users_data = _load_data_from_json()
    if user_id in all_users_data:
        return all_users_data[user_id]
    else:
        return 0, 0


def update_toil_balance(user_id, new_toil_hours):
    """Update the TOIL balance for a user."""
    all_users_data = _load_data_from_json()
    all_users_data[user_id] = (new_toil_hours, new_toil_hours // 8)
    _save_data_to_json(all_users_data)


def get_all_users_data():
    """Get data for all users from the JSON file."""
    all_users_data = _load_data_from_json()
    return [(user_id, toil_hours, toil_hours // 8) for user_id, (toil_hours, _) in all_users_data.items()]


def _load_data_from_json():
    """Load data from the JSON file."""
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return {}


def _save_data_to_json(data):
    """Save data to the JSON file."""
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(data, file)
