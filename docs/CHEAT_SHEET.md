vault operator init
vault kv put secret/my-secret password=my-password
vault kv get secret/my-secret
vault policy write my-policy /path/to/policy.hcl
vault kv list secret/
