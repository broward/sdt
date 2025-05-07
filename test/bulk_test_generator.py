import json
import random
from datetime import datetime

def generate_valid_user_message(tracking_id):
    return {
        "message_type": "user",
        "payload": {
            "header": {
                "message_type": "user",
                "version": 1.0,
                "tracking_id": tracking_id,
                "create_date": datetime.now().strftime("%Y-%m-%d")
            },
            "user_id": random.randint(1000, 9999),
            "first_name": "John",
            "last_name": "Doe",
            "address": {
                "header": {
                    "message_type": "address",
                    "version": 1.0,
                    "tracking_id": tracking_id + 1,
                    "create_date": datetime.now().strftime("%Y-%m-%d")
                },
                "address_1": "123 Main Street",
                "address_2": "Apt 4B",
                "city": "New York",
                "state": "NY",
                "zipcode": "10001",
                "update_date": datetime.now().strftime("%Y-%m-%d")
            },
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "555-123-4567",
            "time_zone": "EST",
            "update_date": datetime.now().strftime("%Y-%m-%d")
        }
    }

def generate_valid_transaction_message(tracking_id):
    return {
        "message_type": "transaction",
        "payload": {
            "header": {
                "message_type": "transaction",
                "version": 1.0,
                "tracking_id": tracking_id,
                "create_date": datetime.now().strftime("%Y-%m-%d")
            },
            "depo_type": random.choice(["gold", "dollar", "other"]),
            "transaction_id": random.randint(1000000, 9999999),
            "payer": random.randint(1000, 5000),
            "payee": random.randint(5001, 9999),
            "amount": round(random.uniform(100.0, 10000.0), 2)
        }
    }

def introduce_error(message):
    error_type = random.choice(["missing_field", "invalid_type", "incorrect_format"])
    payload = message.get("payload", {})
    
    if error_type == "missing_field":
        field_to_remove = random.choice(list(payload.keys()))
        del payload[field_to_remove]
    elif error_type == "invalid_type":
        field_to_modify = "amount" if "amount" in payload else "user_id"
        payload[field_to_modify] = "INVALID_TYPE"
    elif error_type == "incorrect_format":
        field_to_modify = "create_date"
        payload["header"][field_to_modify] = "INVALID_FORMAT"
    return message

def generate_bulk_messages(count, error_chance=0.2):
    messages = []
    tracking_id = 10000

    for _ in range(count):
        tracking_id += 1
        message = random.choice([generate_valid_user_message, generate_valid_transaction_message])(tracking_id)
        if random.random() < error_chance:
            message = introduce_error(message)
        messages.append(message)
    return messages

def save_messages_to_file(messages, file_name="bulk_sdt_messages.json"):
    with open(file_name, "w") as file:
        json.dump(messages, file, indent=4)
    print(f"Generated {len(messages)} messages and saved to {file_name}")

if __name__ == "__main__":
    num_messages = 50  # Adjust the number of messages
    error_rate = 0.2   # 20% of messages will have errors

    bulk_messages = generate_bulk_messages(num_messages, error_rate)
    save_messages_to_file(bulk_messages)

