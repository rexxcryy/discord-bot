import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Bot sudah online sebagai {bot.user}")

@bot.tree.command(name="ping", description="Test bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🟢")

@bot.event
async def setup_hook():
    await bot.tree.sync()

bot.run("TOKEN")

