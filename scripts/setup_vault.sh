#!/bin/bash
# Script pour démarrer Vault en mode développement et créer un secret par défaut

vault server -dev &
sleep 2

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root-token'

# Créer un secret initial
vault kv put secret/my-secret password="my-password"
