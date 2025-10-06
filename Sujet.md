# 🔐 Projet : VaultPass - Gestionnaire de mots de passe sécurisé
## 🎯 Objectif général

Créer un gestionnaire de mots de passe et de notes sécurisé en 3 étapes :

- API en Python (avec chiffrement et JWT)
- Migration vers une base de données SQL multi-utilisateurs
- Interface web simple en PHP

## 🗓️ Semaine 1 : API Python (1 utilisateur - JSON local)

### 💡 Objectif
Créer une API REST en Python qui permet :
- d'enregistrer un utilisateur avec mot de passe (login / signup)
- de se connecter et recevoir un token JWT
- d'ajouter des notes ou mots de passe chiffrés dans un fichier JSON
- de récupérer ses données avec le token JWT

### 🧰 Technologies

- Flask (ou FastAPI)
- PyJWT (JWT)
- Cryptography ou Fernet (pour chiffrer les données)
- Fichier JSON comme base de données temporaire
- Bruno (outil de test API)

### ✅ Fonctionnalités minimales

- POST /signup : créer un utilisateur (hash du mot de passe)
- POST /login : renvoie un token JWT
- POST /vault/add : ajouter une note ou mot de passe (chiffré)
- GET /vault/all : récupérer les données déchiffrées (auth requise)

### 🛡️ Sécurité à enseigner

- JWT : Authentification
- Chiffrement symétrique (Fernet)
- Hash de mot de passe (bcrypt)

## 🗓️ Semaine 2 : Intégration SQL et multi-utilisateurs
### 💡 Objectif

- Remplacer le JSON par une vraie base de données relationnelle SQL. (⚠️ Protection contre les injections sql dans le python)
- Authentification multi-utilisateur
- Gestion des notes/MDP avec jointures SQL 

### 🧰 Technologies

- PostgreSQL ou MySQL (ou SQLite pour simplicité)
- SQLAlchemy (ORM) ou requêtes SQL brutes
- Python (toujours Flask/FastAPI)
- JWT + chiffrement (même logique que semaine 1)

### 🧩 Nouvelle structure

- Table users (id, username, hashed_password)
- Table vault_entries (id, user_id, encrypted_data, type, title, created_at)
- JOIN pour récupérer les données d’un utilisateur

### ✅ Fonctionnalités nouvelles

- Multi-utilisateurs
- Chiffrement toujours côté API
- Authentification JWT reste inchangée
- Sauvegarde dans SQL

## 🗓️ Semaine 3 : Interface web en PHP
### 💡 Objectif

- Créer une interface web simple pour :
- Se connecter
- Voir ses notes / MDP
- Ajouter de nouvelles entrées

### 🧰 Technologies

- PHP (sans framework)
- HTML/CSS minimaliste (Bootstrap éventuellement)
- Appels à l’API Python via les built-in PHP

### ✅ Fonctionnalités

- Formulaire de login → récupère un JWT
- Dashboard : liste des entrées
- Formulaire d’ajout (POST à l’API)
- Authentification via JWT (stocké en session ou localStorage JS)

### 🌱 Évolution possible (bonus ou pour les meilleurs)

- Ajout de dossiers/catégories
- Fonction de recherche dans les notes
- Expiration des tokens JWT
- Authentification 2FA
- Interface JS (React ou Vue)

## 🆒 Barème

| Critère                          | Note |
| -------------------------------- | ---- |
| Fonctionnalité API de base       | 5    |
| Authentification sécurisée (JWT) | 5    |
| Chiffrement/déchiffrement OK     | 5    |
| Base SQL bien utilisée           | 5    |
| Interface PHP fonctionnelle      | 5    |
| Bonus / qualité code / UI        | 5    |
| **Total**                        | /30  |
