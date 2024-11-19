# Discord Bot - Message Automatique

Un bot Discord simple capable de :
- Lire les messages envoyés sur le serveur.
- Répondre à des commandes comme `!test`.
- Envoyer un message privé à tous les membres du serveur via la commande `!send_message`.

## Fonctionnalités
1. **Commande `!test`**  
   - Répond "Le bot fonctionne correctement." pour vérifier que le bot est actif.

2. **Commande `!send_message`**  
   - Envoie un message privé à tous les membres du serveur.  
   - Usage : `!send_message <votre_message>`

3. **Logs en console**  
   - Affiche chaque message reçu par le bot.

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Un bot Discord configuré sur le [Discord Developer Portal](https://discord.com/developers/applications)
- Une clé d'API (Token) du bot

### Étapes
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/0xToto/DiscordBot.git
   cd DiscordBot

2. Installer les dépendances : 
    ```bash
    pip install -r requirements.txt

3. Modifier le fichier main.py pour ajouter le token de votre bot.
    > bot.run("Token")

4. Lancer le bot :
    ```bash
    python Send_member_dm.py


### Exemple d'utilisation : 

[x] !test : Permet de voir si le bot fonctionne correctement
[X] !send_message <Message> : Envoie un message privé à chaque membres qu'ils soient en ligne ou non



### AVERTISSEMENT :

**L'utilisation abusive d'un bot pour envoyer des messages privés peut enfreindre les règles de Discord. Soyez prudent et respectez les conditions d'utilisation de Discord.**
