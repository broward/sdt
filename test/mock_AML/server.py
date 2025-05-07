from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError
import json

with open('schema.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    AML_SCHEMA = json.load(f)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from AML server!"

@app.route("/aml_check", methods=["POST"])
def aml_check():
    data = request.json
    try:
        validate(instance=data, schema=AML_SCHEMA)
        # If compliance_check is true and risk_level is "low" or "medium", return True
        compliance = data["compliance_check"] and data["risk_level"] in ["low", "medium"]
        return jsonify({"success": True, "compliance": compliance}), 200
    except ValidationError as e:
        return jsonify({"success": False, "error": e.message}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
