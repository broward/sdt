import requests

url = "http://127.0.0.1:5000/aml_check"
aml_data = {
    "customer_id": "C123456",
    "transaction_id": "T987654",
    "amount": 2500.50,
    "currency": "USD",
    "transaction_date": "2024-01-01T12:00:00Z",
    "source_of_funds": "Salary",
    "destination_of_funds": "Investment Account",
    "risk_level": "low",
    "compliance_check": True
}

response = requests.post(url, json=aml_data)
print(response.json())
