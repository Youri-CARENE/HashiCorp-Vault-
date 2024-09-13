
# Vault Cheat Sheet

## 1. Démarrer et Initialiser Vault

### Démarrer Vault en mode développement
```bash
vault server -dev
```
- **Explication** : Cette commande démarre Vault en mode développement. Dans ce mode, Vault est non-sécurisé et utilise un token root par défaut. Ce mode est pratique pour tester Vault rapidement, mais ne doit pas être utilisé en production.

### Initialiser Vault en mode production
```bash
vault operator init
```
- **Explication** : Cette commande initialise un serveur Vault en mode production. Elle génère un certain nombre de clés de déverrouillage (unseal keys) et un token root. La sortie inclut plusieurs parties de la clé de déverrouillage que les administrateurs doivent utiliser pour déverrouiller Vault.

---

## 2. Manipulation des Secrets

### Créer ou Mettre à jour un Secret (KV Secrets Engine)
```bash
vault kv put secret/my-secret password=my-password
```
- **Explication** : Cette commande crée ou met à jour un secret sous le chemin `secret/my-secret` avec une paire clé-valeur `password=my-password`. Vault utilise le Secret Engine KV (clé/valeur) pour stocker les données.

### Lire un Secret (KV Secrets Engine)
```bash
vault kv get secret/my-secret
```
- **Explication** : Cette commande lit le secret stocké sous le chemin `secret/my-secret` et affiche ses données.

### Lister les Secrets (KV Secrets Engine)
```bash
vault kv list secret/
```
- **Explication** : Cette commande liste tous les secrets stockés sous le chemin `secret/`. Cela montre les noms des secrets disponibles dans ce chemin, mais pas leurs valeurs.

---

## 3. Politiques de Sécurité

### Créer une Politique
```bash
vault policy write my-policy /path/to/policy.hcl
```
- **Explication** : Cette commande crée ou met à jour une politique nommée `my-policy` en fonction des règles spécifiées dans le fichier HCL (HashiCorp Configuration Language) fourni. Les politiques contrôlent l'accès aux différents chemins dans Vault.

### Exemple d’une politique HCL (`policy.hcl`)
```hcl
path "secret/data/my-secret" {
  capabilities = ["create", "read", "update", "delete"]
}

path "secret/data/*" {
  capabilities = ["list"]
}
```
- **Explication** : Cette politique donne les permissions `create`, `read`, `update`, et `delete` pour le secret spécifique `my-secret`. Pour tous les autres secrets dans `secret/data/`, seule l'action `list` est autorisée.

---

## 4. Gestion des Authentifications

### Activer une méthode d'authentification
```bash
vault auth enable approle
```
- **Explication** : Cette commande active la méthode d'authentification `approle`, qui permet aux applications d'obtenir des tokens d'accès via des rôles définis dans Vault.

### Créer un rôle pour AppRole
```bash
vault write auth/approle/role/my-role \
    secret_id_ttl=10m \
    token_num_uses=10 \
    token_ttl=20m \
    token_max_ttl=30m
```
- **Explication** : Crée un rôle nommé `my-role` avec des paramètres spécifiques pour la gestion des tokens, tels que la durée de validité et le nombre d'utilisations.

### Obtenir le Role ID et Secret ID pour un AppRole
```bash
vault read auth/approle/role/my-role/role-id
vault write -f auth/approle/role/my-role/secret-id
```
- **Explication** : La première commande obtient le `role-id` du rôle `my-role`. La seconde génère un `secret-id` pour ce rôle, nécessaire pour obtenir un token d'accès.

---

## 5. Gestion de l'État de Vault

### Verrouiller (Sealer) Vault
```bash
vault operator seal
```
- **Explication** : Cette commande verrouille (scelle) Vault, rendant tous les secrets inaccessibles jusqu'à ce que Vault soit déverrouillé.

### Déverrouiller (Unseal) Vault
```bash
vault operator unseal <unseal-key>
```
- **Explication** : Utilisez cette commande avec l'une des clés de déverrouillage générées lors de l'initialisation pour déverrouiller Vault. Cette commande doit être exécutée plusieurs fois (selon le seuil configuré) jusqu'à ce que Vault soit entièrement déverrouillé.

---

## 6. Commandes Utiles Diverses

### Lister les méthodes d'authentification activées
```bash
vault auth list
```
- **Explication** : Cette commande liste toutes les méthodes d'authentification activées sur le serveur Vault.

### Lister les moteurs de secrets activés
```bash
vault secrets list
```
- **Explication** : Cette commande affiche les différents moteurs de secrets activés, ainsi que les chemins associés.

### Révoquer un token
```bash
vault token revoke <token-id>
```
- **Explication** : Cette commande révoque un token spécifique, rendant tout accès via ce token invalide.

### Activer un Secret Engine
```bash
vault secrets enable -path=kv kv-v2
```
- **Explication** : Active un moteur de secrets KV version 2 sous le chemin `kv`. Ce moteur permet le versionnement des secrets.
