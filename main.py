# All In One Bot - Made By lordxStar
# Watermark: lordxStar

import discord
from discord.ext import commands
import json
import os

# Load config (token, prefix, etc.)
def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=config.get("prefix", "!"),
    intents=intents,
    help_command=None  # Custom help
)

# --- EVENTS --- #
@bot.event
async def on_ready():
    print("===================================")
    print(f"Logged in as: {bot.user} (ID: {bot.user.id})")
    print("All In One Bot - Made By lordxStar")
    print("===================================")
    await bot.change_presence(
        activity=discord.Game(name="All In One Bot - Made By lordxStar")
    )

# --- LOAD COGS --- #
initial_cogs = ["cogs.fun", "cogs.moderation", "cogs.utility"]

@bot.command(name="reload")
@commands.is_owner()
async def reload_cogs(ctx):
    """Reload all cogs (Owner only) - Made By lordxStar"""
    for ext in initial_cogs:
        try:
            bot.reload_extension(ext)
        except commands.ExtensionNotLoaded:
            bot.load_extension(ext)
    await ctx.send("♻️ All cogs reloaded! - Made By lordxStar")

@bot.command(name="help")
async def custom_help(ctx):
    """Simple custom help command - Made By lordxStar"""
    prefix = config.get("prefix", "!")
    embed = discord.Embed(
        title="All In One Bot - Help",
        description=f"Made By **lordxStar**\nPrefix: `{prefix}`",
    )
    embed.add_field(
        name="🎉 Fun",
        value=f"`{prefix}ping`, `{prefix}hello`, `{prefix}echo`",
        inline=False
    )
    embed.add_field(
        name="🛡️ Moderation",
        value=f"`{prefix}kick`, `{prefix}ban`, `{prefix}clear`",
        inline=False
    )
    embed.add_field(
        name="🧰 Utility",
        value=f"`{prefix}userinfo`, `{prefix}serverinfo`",
        inline=False
    )
    embed.set_footer(text="All In One Bot - Made By lordxStar")
    await ctx.send(embed=embed)

# Auto load cogs on startup
if __name__ == "__main__":
    for ext in initial_cogs:
        try:
            bot.load_extension(ext)
            print(f"Loaded extension: {ext}")
        except Exception as e:
            print(f"Failed to load {ext}: {e}")

    bot.run(config["token"])
