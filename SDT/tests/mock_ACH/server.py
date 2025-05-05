from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError
import json

with open('schema.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    ACH_SCHEMA = json.load(f)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from ACH server!" + str(ACH_SCHEMA)

@app.route("/ach_transaction", methods=["POST"])
def ach_transaction():
    data = request.json
    try:
        validate(instance=data, schema=ACH_SCHEMA)
        # Validation passed, transaction is valid
        return jsonify({"success": True, "valid": True}), 200
    except ValidationError as e:
        # Validation failed
        return jsonify({"success": False, "error": e.message}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)

