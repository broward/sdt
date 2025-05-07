if __name__ == "__main__":
    rpc_url = "http://127.0.0.1:8545"  # Replace with your Quorum node's JSON-RPC URL
    client = QuorumClient(rpc_url)

    # Example 1: Send a transaction
    from_address = "0xSenderAddressHere"
    to_address = "0xRecipientAddressHere"
    value_in_wei = 1000000000000000000  # 1 Ether
    private_for = ["PublicKey1", "PublicKey2"]  # For private transactions

    print("Sending transaction...")
    try:
        tx_hash = client.send_transaction(from_address, to_address, value_in_wei, private_for)
        print(f"Transaction sent successfully. Hash: {tx_hash['result']}")
    except Exception as e:
        print(f"Failed to send transaction: {e}")

    # Example 2: Get transaction details
    print("\nRetrieving transaction details...")
    try:
        transaction_hash = tx_hash["result"]  # Replace with a valid transaction hash
        transaction_details = client.get_transaction(transaction_hash)
        print("Transaction details:")
        print(json.dumps(transaction_details, indent=4))
    except Exception as e:
        print(f"Failed to retrieve transaction: {e}")
