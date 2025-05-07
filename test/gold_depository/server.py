from flask import Flask, request, jsonify
import json

with open('schema.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    GOLD_SCHEMA = json.load(f)

app = Flask(__name__)

# Mock database
coins = {}

@app.route("/")
def index():
    return "Hello from GOLD server!"

@app.route('/coins', methods=['POST'])
def add_coin():
    data = request.json
    coin_id = data.get('coin_id')
    if coin_id in coins:
        return jsonify({"success": False, "message": "Coin already exists."}), 400
    coins[coin_id] = {
        "description": data["description"],
        "owners": {data["current_owner"]: 1.0},
        "value": data["value"],
        "creation_date": data["creation_date"]
    }
    return jsonify({"success": True, "message": "Coin added successfully."})

@app.route('/coins/<coin_id>/transfer', methods=['POST'])
def transfer_ownership(coin_id):
    data = request.json
    from_owner = data["from_owner"]
    to_owner = data["to_owner"]
    fraction = data["fraction"]

    if coin_id not in coins or from_owner not in coins[coin_id]["owners"]:
        return jsonify({"success": False, "message": "Coin or owner not found."}), 404

    current_fraction = coins[coin_id]["owners"].get(from_owner, 0)
    if current_fraction < fraction:
        return jsonify({"success": False, "message": "Insufficient ownership to transfer."}), 400

    # Deduct from current owner
    coins[coin_id]["owners"][from_owner] -= fraction
    if coins[coin_id]["owners"][from_owner] == 0:
        del coins[coin_id]["owners"][from_owner]

    # Add to new owner
    coins[coin_id]["owners"][to_owner] = coins[coin_id]["owners"].get(to_owner, 0) + fraction

    return jsonify({"success": True, "message": "Ownership transferred."})

@app.route('/coins/<coin_id>', methods=['GET'])
def get_coin(coin_id):
    if coin_id not in coins:
        return jsonify({"success": False, "message": "Coin not found."}), 404
    return jsonify({"success": True, "coin": coins[coin_id]})

@app.route('/coins', methods=['GET'])
def list_coins():
    return jsonify({"success": True, "coins": list(coins.keys())})

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5004)
