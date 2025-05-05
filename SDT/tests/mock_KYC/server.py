from flask import Flask, request, jsonify
import json

with open('schema.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    KYC_SCHEMA = json.load(f)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from KYC server!"

# Endpoint to receive KYC information
@app.route("/submit_kyc", methods=["POST"])
def submit_kyc():
    data = request.json

    # Validate JSON payload against schema
    from jsonschema import validate, ValidationError

    try:
        validate(instance=data, schema=KYC_SCHEMA)
        return jsonify({"success": True}), 200
    except ValidationError as e:
        return jsonify({"success": False, "error": e.message}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
