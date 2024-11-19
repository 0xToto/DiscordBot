import discord
from discord.ext import commands

# Définir les intentions nécessaires
intents = discord.Intents.default()
intents.members = True  # Accès aux membres
intents.message_content = True  # Lecture du contenu des messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    print(f"Message reçu : {message.content} par {message.author}")
    await bot.process_commands(message)  # Nécessaire pour que les commandes fonctionnent

@bot.command()
async def test(ctx):
    await ctx.send("Le bot fonctionne correctement.")

@bot.command()
async def send_message(ctx, *, message: str):
    """Envoie un message privé à tous les membres du serveur."""
    if not ctx.guild:  # Vérifie que la commande est utilisée dans un serveur
        await ctx.send("Cette commande doit être exécutée dans un serveur.")
        return

    # Confirmation de démarrage
    await ctx.send("Envoi des messages en cours...")

    members = ctx.guild.members  # Liste des membres du serveur
    success = 0
    failed = 0

    for member in members:
        if member.bot:  # Ignorer les bots
            continue
        try:
            # Envoi du message
            await member.send(message)
            print(f"Message envoyé à {member.name}")
            success += 1
        except Exception as e:
            print(f"Impossible d'envoyer un message à {member.name}: {e}")
            failed += 1

    # Résumé après l'envoi
    await ctx.send(f"Messages envoyés avec succès : {success}, Échecs : {failed}")
bot.run("Token Bot")