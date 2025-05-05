transaction = fireblocks.create_transaction(
    asset_id="BTC",
    source={
        "type": "VAULT_ACCOUNT",
        "id": "vault_account_id"
    },
    destination={
        "type": "ONE_TIME_ADDRESS",
        "oneTimeAddress": {
            "address": "testnet_btc_address"
        }
    },
    amount=0.01,
    fee_level="HIGH",
    note="Testing external shard integration"
)
print("Transaction initiated:", transaction)
