import os
from sdt.config_loader import ConfigLoader
from sdt.mapper.mapper import SingletonJSONLoader

# Ensure SDT_ENV is set in the environment
os.environ["SDT_ENV"] = "test"  # Set this for testing purposes

# Usage example
if __name__ == "__main__":
    
    env = ConfigLoader()
    print("aml:", env.get(env.AML_SERVER))
    print("kyc:", env.get(env.KYC_SERVER))
    print("API_KEY:", env.get(env.SECRETS_STORE).get(env.SS_ACCESS_KEY))
    
    loader = SingletonJSONLoader()
    print("loader done")

    # Access loaded data
    for file_path in loader.get_loaded_files():
        data = loader.get_data("kyc_keymap.json")
        print(f"Data from {file_path}: {data}")


