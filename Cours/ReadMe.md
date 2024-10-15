# Vault Zero to Hero

Bienvenue dans le projet **Vault Zero to Hero**. Ce dépôt est destiné à enseigner et démontrer l'utilisation de HashiCorp Vault à travers trois sections principales : **Cours**, **Installation**, et un **Exemple de Projet** pratique.

## Cours

### Introduction à Vault
HashiCorp Vault est un outil permettant de gérer de manière sécurisée les secrets et autres données sensibles. Il peut être utilisé pour stocker et accéder aux informations confidentielles, telles que les mots de passe, les clés API, les certificats, etc. Vault permet de centraliser et sécuriser ces données, tout en fournissant un accès contrôlé grâce à des mécanismes tels que les tokens et les politiques d'accès.

### Concepts de base
- **Gestion des Secrets** : Vault permet de stocker des secrets (comme des mots de passe) sous forme de données clés-valeurs. Ces secrets peuvent être récupérés et utilisés via l'API de Vault ou en ligne de commande.
- **Tokens** : Chaque interaction avec Vault nécessite un token qui contrôle les autorisations et le temps d'accès.
- **Politiques** : Les politiques définissent les permissions d'accès pour chaque utilisateur ou service. Cela permet un contrôle fin sur ce à quoi chaque entité a accès dans Vault.
- **Approbations (Leases)** : Vault accorde des autorisations temporaires (leases) pour accéder aux secrets. Ces approbations peuvent être renouvelées ou révoquées manuellement ou automatiquement.

### Bonnes pratiques
- **Sécuriser l'accès** : Utiliser TLS pour chiffrer les communications entre Vault et les clients.
- **Rotation régulière des secrets** : Les secrets ne devraient pas être stockés indéfiniment. Vault peut automatiser la rotation des secrets.
- **Minimalisme des permissions** : Chaque token ou rôle doit avoir le moins de permissions possible pour accomplir sa tâche.
  
Pour des explications plus détaillées sur ces concepts, vous pouvez consulter [CHEAT_SHEET.md](CHEAT_SHEET.md) et [Concepts_Vault.md](Concepts_Vault.md).

## Installation

### Prérequis
- **Docker** : Assurez-vous que Docker est installé sur votre machine.
- **Vault** : Vous pouvez installer Vault en utilisant le binaire ou l'exécuter via Docker.

### Installation avec Docker (mode développement)
Pour démarrer rapidement avec Vault en mode développement, utilisez le script `setup_vault.sh` :

```bash
bash scripts/setup_vault.sh
