# 🎉 ALL IN ONE BOT – Made By lordxStar

A powerful all-in-one Discord bot built with Python (discord.py) including Moderation, Utility, Fun commands, custom help menu, and more.


---

🌟 Features

Category	Commands

🎉 Fun	ping, hello, echo, 8ball, reverse
🛡️ Moderation	kick, ban, clear, slowmode, nick
🧰 Utility	userinfo, serverinfo, avatar, botinfo


All commands include watermark Made By lordxStar inside the bot.


---

📂 Project Structure

all-in-one-bot/
│ bot.py
│ config.example.json
│ requirements.txt
│ README.md
│ .gitignore
└── cogs/
    │ __init__.py
    │ fun.py
    │ moderation.py
    │ utility.py


---

🔧 Installation & Setup

1️⃣ Install Python

Download latest Python from https://python.org (version 3.10+ recommended).

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Create config.json

Create config.json manually:

{
  "token": "YOUR_BOT_TOKEN_HERE",
  "prefix": "!"
}

> ⚠ Never upload real token to GitHub.



4️⃣ Run the bot

python bot.py


---

🎮 All Commands List

🎉 Fun Commands

Command	Description

!ping	Shows bot latency 🏓
!hello	Say hello 👋
!echo <text>	Repeats your message
!8ball <question>	Random yes/no response 🎱
!reverse <text>	Reverses text 🔁


🛡️ Moderation Commands

Command	Requires Permission	Description

!kick @user [reason]	Kick Members	Kick user 🦵
!ban @user [reason]	Ban Members	Ban user ⛔
!clear <amount>	Manage Messages	Clears chat messages 🧹
!slowmode <seconds>	Manage Channels	Enable / disable slowmode ⏱
!nick @user <newname>	Manage Nicknames	Change/reset nickname ✏️


🧰 Utility Commands

Command	Description

!userinfo [user]	Shows profile info 👤
!serverinfo	Shows server info 🏛️
!avatar [user]	Shows profile picture 🖼
!botinfo	Shows bot details 🤖



---

⚙ .gitignore Example

config.json
__pycache__/
.env


---

💡 Custom Help Command Preview

!help

Displays categories + watermark by lordxStar


---

💝 Credits

All In One Bot – Made By lordxStar
Watermark Included In All Files

If you want extra features (Music bot, Level system, Ticket system, AI chat, Auto moderation), ask anytime 💫
