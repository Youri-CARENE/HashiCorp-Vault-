import hvac

class VaultManager:
    def __init__(self, url, token):
        self.client = hvac.Client(url=url, token=token)
    
    def create_secret(self, secret_path, secret_data):
        # Stocker un secret dans Vault
        self.client.secrets.kv.v2.create_or_update_secret(path=secret_path, secret=secret_data)
    
    def read_secret(self, secret_path):
        # Lire un secret depuis Vault
        return self.client.secrets.kv.v2.read_secret_version(path=secret_path)

# Exemple d’utilisation
if __name__ == "__main__":
    vault_url = "http://127.0.0.1:8200"
    vault_token = "root-token"
    
    manager = VaultManager(url=vault_url, token=vault_token)
    
    # Créer un secret
    manager.create_secret("my-secret", {"password": "my-password"})
    
    # Lire le secret
    secret = manager.read_secret("my-secret")
    print(f"Secret fetched: {secret['data']['data']}")
