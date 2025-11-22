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

Displays categories + wat
``` ⚔️ All In One Bot — Made By lordxStar

A multi‑feature Discord bot packed with **Moderation, Utility, Fun, Music, Database + Config System**.

---

## 🧠 Setup
```bash
python main.py


---

-------|-----------| | !play <song/url> | Play a track | | !pause | Pause playback | | !resume | Resume playback | | !skip | Skip current song | | !stop | Stop player | | !nowplaying | Show current track | | !queue | Show queue | | !autoplay | Toggle autoplay | | !volume <1‑5000> | Change volume | | !lofi | Enable lofi filter |


---

🛡️ Moderation Commands

Command	Function

!kick @user	Kick user
!ban @user	Ban user
!unban name#0000	Unban member
!clear <amount>	Clear messages
!slowmode <sec>	Enable slowmode
!nick @user <name>	Change nickname
!warn @user <reason>	Warn member
!warnings @user	View warnings
!lock	Lock channel
!unlock	Unlock channel



---

🎉 Fun Commands

Command	Function

!ping	Check latency
!hello	Say Hello
!echo <msg>	Repeat text
!8ball <ask>	Random answer
!reverse <text>	Reverse text
!choose a b c	Random choice



---

🧰 Utility Commands

Command	Function

!userinfo	User information
!serverinfo	Server stats
!avatar	Show profile image
!botinfo	Bot info
!uptime	Show uptime
!poll	Create poll



---

📂 File Structure

config.json
config.example.json
main.py
database.py
requirements.txt
.gitignore
README.md
/data


---

📌 Disclaimer

This project is for educational purposes only. Use responsibly. Do not violate Discord Terms of Service.


---

👑 Credits

Developed by lordxStar

> Respect credits — Removing credits means you don’t respect the creator.
