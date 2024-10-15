# Vault Knowledge Base

## Qu'est-ce que Vault ?
Vault est un gestionnaire de secrets développé par HashiCorp. Il permet de stocker et de gérer des informations sensibles (secrets) telles que des tokens API, mots de passe, certificats, etc.

### Concepts clés :
1. **Secrets Engines** : Mécanismes permettant de gérer différents types de secrets (clé/valeur, certificats dynamiques, etc.).
2. **Policies** : Règles qui définissent l'accès aux secrets.
3. **Authentication Methods** : Méthodes pour vérifier l'identité de l'utilisateur ou du système (ex: Token, AppRole, LDAP).
4. **Dynamic Secrets** : Secrets générés à la demande, souvent utilisés avec des bases de données ou des services cloud.

### Pourquoi utiliser Vault ?
- Sécurisation centralisée des secrets
- Gestion des accès basée sur des politiques
- Intégration facile avec les systèmes existants (Kubernetes, Docker, Terraform, etc.)

### Structure d'un Secret Engine KV
- Les secrets sont stockés sous forme de paires clé-valeur.
- Vault offre deux versions du Secret Engine KV : Version 1 (sans versionnement) et Version 2 (avec versionnement des secrets).
