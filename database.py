
# All In One Bot - Database Module
# Made By lordxStar

import aiosqlite
import os

DB_PATH = os.path.join("data", "bot.db")


async def init_db():
    """Initialize database and tables - Made By lordxStar"""
    os.makedirs("data", exist_ok=True)

    async with aiosqlite.connect(DB_PATH) as db:
        # Warning system table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS warnings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guild_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                moderator_id INTEGER NOT NULL,
                reason TEXT,
                timestamp TEXT
            )
        """)

        # Guild settings table (for future use)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS guild_settings (
                guild_id INTEGER PRIMARY KEY,
                prefix TEXT,
                welcome_channel INTEGER
            )
        """)

        await db.commit()


async def add_warning(guild_id: int, user_id: int, moderator_id: int, reason: str, timestamp: str):
    """Add warning to database - Made By lordxStar"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO warnings (guild_id, user_id, moderator_id, reason, timestamp) VALUES (?, ?, ?, ?, ?)",
            (guild_id, user_id, moderator_id, reason, timestamp)
        )
        await db.commit()


async def get_warnings(guild_id: int, user_id: int):
    """Get all warnings for user in a guild - Made By lordxStar"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT id, moderator_id, reason, timestamp FROM warnings WHERE guild_id = ? AND user_id = ?",
            (guild_id, user_id)
        )
        rows = await cursor.fetchall()
        await cursor.close()
        return rows
