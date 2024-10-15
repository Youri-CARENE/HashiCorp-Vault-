# Utilisation de l’image Python
FROM python:3.9-slim

# Installer les dépendances
RUN pip install hvac

# Copier le code source dans le conteneur
COPY ./src /app/src
WORKDIR /app/src

# Exposer le port de Vault (si besoin pour les tests)
EXPOSE 8200

# Lancer le fichier principal
CMD ["python", "main.py"]
