import pytest
from vault_manager import VaultManager

@pytest.fixture
def vault_manager():
    return VaultManager(url="http://127.0.0.1:8200", token="root-token")

def test_create_and_read_secret(vault_manager):
    secret_path = "test-secret"
    secret_data = {"username": "admin", "password": "password123"}
    
    # Créer un secret
    vault_manager.create_secret(secret_path, secret_data)
    
    # Lire le secret
    retrieved_secret = vault_manager.read_secret(secret_path)
    assert retrieved_secret['data']['data'] == secret_data
