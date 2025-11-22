"""
All In One Bot - Made By lordxStar
Uses external config.json for settings.
"""

import discord
from discord.ext import commands
import json
from datetime import datetime

# LOAD CONFIG =======================
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["token"]
PREFIX = config["prefix"]
OWNER_ID = int(config["owner_id"])
EMBED_COLOR = int(config["embed_color"].replace("#", ""), 16)
WELCOME_CHANNEL_ID = int(config["welcome_channel"])
WATERMARK = config["watermark"]

# BOT SETUP =========================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    help_command=None
)

start_time = datetime.utcnow()


# EVENTS ============================
@bot.event
async def on_ready():
    print("===================================")
    print(f"Logged in as {bot.user} | ID: {bot.user.id}")
    print("All In One Bot - Made By lordxStar")
    print("===================================")
    await bot.change_presence(
        activity=discord.Game(name=WATERMARK)
    )


# HELP COMMAND ======================
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="All In One Bot - Help",
        description=WATERMARK,
        color=EMBED_COLOR
    )
    embed.add_field(
        name="🎉 Fun",
        value="`ping`, `hello`, `echo`, `8ball`, `reverse`",
        inline=False
    )
    embed.add_field(
        name="🛡️ Moderation",
        value="`kick`, `ban`, `clear`, `slowmode`, `nick`",
        inline=False
    )
    embed.add_field(
        name="🧰 Utility",
        value="`userinfo`, `serverinfo`, `avatar`, `botinfo`",
        inline=False
    )
    embed.set_footer(text=WATERMARK)
    await ctx.send(embed=embed)


# SIMPLE COMMAND ====================
@bot.command()
async def ping(ctx):
    """Check bot latency"""
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms - {WATERMARK}")


# RUN BOT ===========================
if __name__ == "__main__":
    bot.run(TOKEN)
