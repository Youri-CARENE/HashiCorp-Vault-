from vault_manager import VaultManager

def main():
    vault_url = "http://127.0.0.1:8200"
    vault_token = "root-token"
    
    vault_manager = VaultManager(url=vault_url, token=vault_token)
    
    secret_path = "demo-secret"
    secret_data = {"api_key": "1234567890"}
    
    # Ajouter un secret
    vault_manager.create_secret(secret_path, secret_data)
    
    # Lire un secret
    retrieved_secret = vault_manager.read_secret(secret_path)
    print(f"Secret fetched: {retrieved_secret['data']['data']}")

if __name__ == "__main__":
    main()
