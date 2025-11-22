
"""
====================================================
   All In One Discord Bot - Made By lordxStar
====================================================
Professional Python Discord bot powered by discord.py
Includes Moderation, Utility, Fun, XP System & DB Warnings
====================================================
"""

import discord
import json
import asyncio
import logging
from discord.ext import commands
from datetime import datetime

# Database functions (from database.py)
try:
    from database import init_db, add_warning, get_warnings
except ImportError:
    init_db = None
    add_warning = None
    get_warnings = None

# ===============================================
# LOAD CONFIG
# ===============================================
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = config["token"]
PREFIX = config["prefix"]
OWNER_ID = int(config["owner_id"])
EMBED_COLOR = int(config["embed_color"].replace("#", ""), 16)
WELCOME_CHANNEL_ID = int(config["welcome_channel"])
WATERMARK = config["watermark"]

# ===============================================
# LOGGING SYSTEM
# ===============================================
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("lordxStarBot")

# ===============================================
# BOT SETUP
# ===============================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    help_command=None,
)

start_time = datetime.utcnow()

# In-memory XP system {user_id: {"xp": int, "level": int}}
xp_data = {}

# ===============================================
# OWNER CHECK
# ===============================================
def is_owner():
    async def predicate(ctx):
        return ctx.author.id == OWNER_ID
    return commands.check(predicate)

# ===============================================
# EVENTS
# ===============================================
@bot.event
async def on_ready():
    logger.info("============================================")
    logger.info(f"Logged in as: {bot.user} | ID: {bot.user.id}")
    logger.info("All In One Bot - Made By lordxStar")
    logger.info(f"Prefix: {PREFIX} | Owner ID: {OWNER_ID}")
    logger.info("============================================")

    await bot.change_presence(
        activity=discord.Game(name=WATERMARK)
    )

    # Init DB if available
    if init_db is not None:
        try:
            await init_db()
            logger.info("Database initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")

    print("\n🚀 Bot Started Successfully!")
    print("👑 Owner:", OWNER_ID)
    print("🔧 Prefix:", PREFIX)


@bot.event
async def on_member_join(member: discord.Member):
    if WELCOME_CHANNEL_ID != 0:
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title="🎉 Welcome",
                description=f"Welcome to **{member.guild.name}**, {member.mention}!",
                color=EMBED_COLOR,
            )
            embed.set_footer(text=WATERMARK)
            try:
                embed.set_thumbnail(url=member.display_avatar.url)
            except Exception:
                pass
            await channel.send(embed=embed)


@bot.event
async def on_message(message: discord.Message):
    # Ignore bot messages
    if message.author.bot:
        return

    # XP system
    user_id = message.author.id
    data = xp_data.get(user_id, {"xp": 0, "level": 0})
    data["xp"] += 5  # XP per message
    new_level = int(data["xp"] ** 0.5)  # simple level formula

    if new_level > data["level"]:
        data["level"] = new_level
        xp_data[user_id] = data
        try:
            await message.channel.send(
                f"⭐ {message.author.mention} leveled up to **Level {new_level}**!"
            )
        except Exception:
            pass
    else:
        xp_data[user_id] = data

    # Process commands
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Missing required argument.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Invalid argument.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"⏳ Wait `{error.retry_after:.1f}s` before using this again.")
    else:
        logger.error(f"Unexpected error: {error}")
        await ctx.send("⚠ An unexpected error occurred.")

# ===============================================
# CUSTOM HELP
# ===============================================
@bot.command()
async def help(ctx: commands.Context):
    embed = discord.Embed(
        title="⚔️ All In One Bot — Help Menu",
        description=f"Made By **lordxStar**\nPrefix: `{PREFIX}`",
        color=EMBED_COLOR,
    )
    embed.add_field(
        name="🛡 Moderation",
        value="`kick`, `ban`, `unban`, `clear`, `slowmode`, `nick`, `warn`, `warnings`, `lock`, `unlock`",
        inline=False,
    )
    embed.add_field(
        name="🎉 Fun",
        value="`ping`, `hello`, `echo`, `8ball`, `reverse`, `choose`, `say`",
        inline=False,
    )
    embed.add_field(
        name="🧰 Utility",
        value="`userinfo`, `serverinfo`, `avatar`, `botinfo`, `uptime`, `poll`",
        inline=False,
    )
    embed.add_field(
        name="👑 Owner",
        value="`shutdown`, `ownerping`, `syncstatus`",
        inline=False,
    )
    embed.set_footer(text=WATERMARK)
    await ctx.send(embed=embed)

# ===============================================
# OWNER COMMANDS
# ===============================================
@bot.command()
@is_owner()
async def shutdown(ctx: commands.Context):
    """Owner only: shutdown bot"""
    await ctx.send("⚠ Shutting down... (Owner Command)")
    logger.info("Shutdown requested by owner.")
    await bot.close()


@bot.command()
@is_owner()
async def ownerping(ctx: commands.Context):
    """Owner only: ping with extra debug"""
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"👑 Owner Pong: `{latency_ms}ms`")


@bot.command()
@is_owner()
async def syncstatus(ctx: commands.Context, *, status: str = None):
    """Owner only: change bot status"""
    if not status:
        status = WATERMARK
    await bot.change_presence(activity=discord.Game(name=status))
    await ctx.send(f"✅ Status updated to: `{status}`")

# ===============================================
# FUN COMMANDS
# ===============================================
@bot.command()
async def ping(ctx: commands.Context):
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong: `{latency_ms}ms` - {WATERMARK}")


@bot.command()
async def hello(ctx: commands.Context):
    await ctx.send(f"Hello {ctx.author.mention}! 👋 — **{WATERMARK}**")


@bot.command()
async def echo(ctx: commands.Context, *, message: str):
    await ctx.send(message)


@bot.command(name="8ball")
async def eight_ball(ctx: commands.Context, *, question: str):
    import random

    responses = [
        "Yes ✅",
        "No ❌",
        "Maybe 🤔",
        "Definitely 🔥",
        "Not sure, try again 🕒",
        "Probably yes ✨",
        "I don't think so 😶",
        "50-50 😅",
    ]
    await ctx.send(
        f"🎱 **Question:** {question}\n**Answer:** {random.choice(responses)}"
    )


@bot.command()
async def reverse(ctx: commands.Context, *, text: str):
    await ctx.send(text[::-1])


@bot.command()
async def choose(ctx: commands.Context, *options: str):
    import random

    if len(options) < 2:
        return await ctx.send("❌ Provide at least 2 options.")
    await ctx.send(f"🎲 I choose: **{random.choice(options)}**")


@bot.command()
async def say(ctx: commands.Context, *, message: str):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    await ctx.send(message)

# ===============================================
# MODERATION COMMANDS
# ===============================================
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = "No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(f"🦵 Kicked {member.mention} | Reason: `{reason}` | By **{ctx.author}**")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = "No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(f"⛔ Banned {member.mention} | Reason: `{reason}` | By **{ctx.author}**")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx: commands.Context, *, user: str):
    """Unban by name#discriminator"""
    banned_users = await ctx.guild.fetch_bans()
    name, discriminator = user.split("#")

    for ban_entry in banned_users:
        banned_user = ban_entry.user
        if (banned_user.name, banned_user.discriminator) == (name, discriminator):
            await ctx.guild.unban(banned_user)
            await ctx.send(f"✅ Unbanned {banned_user.mention}")
            return

    await ctx.send("❌ User not found in ban list.")


@bot.command(name="clear", aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx: commands.Context, amount: int = 10):
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(
        f"🧹 Deleted `{len(deleted)-1}` messages.",
        delete_after=5,
    )


@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx: commands.Context, seconds: int = 0):
    if seconds < 0:
        seconds = 0
    await ctx.channel.edit(slowmode_delay=seconds)
    if seconds == 0:
        await ctx.send("⏱ Slowmode disabled.")
    else:
        await ctx.send(f"⏱ Slowmode set to `{seconds}` seconds.")


@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx: commands.Context, member: discord.Member, *, nickname: str = None):
    await member.edit(nick=nickname)
    if nickname:
        await ctx.send(f"✏️ Nickname changed to `{nickname}` for {member.mention}.")
    else:
        await ctx.send(f"✏️ Nickname reset for {member.mention}.")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx: commands.Context, member: discord.Member, *, reason: str = "No reason provided"):
    """Warn a user and store it in DB if configured."""
    timestamp = datetime.utcnow().isoformat(sep=" ", timespec="seconds")

    if add_warning is not None:
        try:
            await add_warning(
                guild_id=ctx.guild.id,
                user_id=member.id,
                moderator_id=ctx.author.id,
                reason=reason,
                timestamp=timestamp,
            )
            await ctx.send(
                f"⚠ Warned {member.mention} | Reason: `{reason}` (saved in database)"
            )
            return
        except Exception as e:
            logger.error(f"Failed to add warning to DB: {e}")

    # Fallback if DB not available
    await ctx.send(
        f"⚠ Warned {member.mention} | Reason: `{reason}` (DB not configured properly)"
    )


@bot.command(name="warnings")
async def warnings_cmd(ctx: commands.Context, member: discord.Member = None):
    """View warnings for a user"""
    member = member or ctx.author

    if get_warnings is None:
        return await ctx.send("❌ Warning database not configured.")

    try:
        rows = await get_warnings(ctx.guild.id, member.id)
    except Exception as e:
        logger.error(f"Failed to fetch warnings: {e}")
        return await ctx.send("❌ Failed to fetch warnings from database.")

    if not rows:
        return await ctx.send(f"✅ {member.mention} has no warnings.")

    description = ""
    for idx, (warn_id, mod_id, reason, timestamp) in enumerate(rows, start=1):
        description += f"`{idx}.` **Mod:** <@{mod_id}> | **Reason:** {reason} | `{timestamp}`\n"

    embed = discord.Embed(
        title=f"⚠ Warnings for {member}",
        description=description,
        color=EMBED_COLOR,
    )
    embed.set_footer(text=WATERMARK)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx: commands.Context):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔒 Channel locked.")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx: commands.Context):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔓 Channel unlocked.")

# ===============================================
# UTILITY COMMANDS
# ===============================================
@bot.command()
async def userinfo(ctx: commands.Context, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(
        title=f"User Info — {member}",
        description=f"ID: `{member.id}`",
        color=EMBED_COLOR,
    )
    embed.add_field(
        name="Account Created",
        value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        inline=False,
    )
    if member.joined_at:
        embed.add_field(
            name="Joined Server",
            value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=False,
        )
    embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
    try:
        embed.set_thumbnail(url=member.display_avatar.url)
    except Exception:
        pass
    embed.set_footer(text=WATERMARK)
    await ctx.send(embed=embed)


@bot.command()
async def serverinfo(ctx: commands.Context):
    guild = ctx.guild
    embed = discord.Embed(
        title=f"Server Info — {guild.name}",
        description=f"ID: `{guild.id}`",
        color=EMBED_COLOR,
    )
    embed.add_field(name="Owner", value=str(guild.owner), inline=False)
    embed.add_field(name="Members", value=guild.member_count, inline=False)
    embed.add_field(
        name="Created At",
        value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        inline=False,
    )
    if guild.icon:
        try:
            embed.set_thumbnail(url=guild.icon.url)
        except Exception:
            pass
    embed.set_footer(text=WATERMARK)
    await ctx.send(embed=embed)


@bot.command()
async def avatar(ctx: commands.Context, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(
        title=f"Avatar — {member}",
        color=EMBED_COLOR,
    )
    try:
        embed.set_image(url=member.display_avatar.url)
    except Exception:
        pass
    embed.set_footer(text=WATERMARK)
    await ctx.send(embed=embed)


@bot.command()
async def botinfo(ctx: commands.Context):
    embed = discord.Embed(
        title="Bot Info",
        description=f"All In One Bot - Made By **lordxStar**",
        color=EMBED_COLOR,
    )
    embed.add_field(name="Bot Name", value=bot.user.name, inline=True)
    embed.add_field(name="Bot ID", value=bot.user.id, inline=True)
    embed.add_field(name="Servers", value=len(bot.guilds), inline=True)
    embed.set_footer(text=WATERMARK)
    try:
        embed.set_thumbnail(url=bot.user.display_avatar.url)
    except Exception:
        pass
    await ctx.send(embed=embed)


@bot.command()
async def uptime(ctx: commands.Context):
    now = datetime.utcnow()
    delta = now - start_time
    total_seconds = int(delta.total_seconds())
    days, rem = divmod(total_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    resp = f"{days}d {hours}h {minutes}m {seconds}s"
    await ctx.send(f"⏱ Uptime: `{resp}`")


@bot.command()
async def poll(ctx: commands.Context, question: str, *, options: str = None):
    if options is None:
        return await ctx.send("❌ Provide options separated by commas.")

    option_list = [opt.strip() for opt in options.split(",") if opt.strip()]
    if len(option_list) < 2:
        return await ctx.send("❌ Provide at least 2 options.")
    if len(option_list) > 10:
        return await ctx.send("❌ Max 10 options allowed.")

    emojis = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

    description = ""
    for i, opt in enumerate(option_list):
        description += f"{emojis[i]} {opt}\n"

    embed = discord.Embed(
        title=f"📊 {question}",
        description=description,
        color=EMBED_COLOR,
    )
    embed.set_footer(text=WATERMARK)
    msg = await ctx.send(embed=embed)

    for i in range(len(option_list)):
        await msg.add_reaction(emojis[i])

# ===============================================
# RUN BOT
# ===============================================
if __name__ == "__main__":
    if not TOKEN or TOKEN == "YOUR_BOT_TOKEN_HERE":
        raise ValueError("⚠ Please set a valid token in config.json before running.")
    bot.run(TOKEN)
