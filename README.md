# Telegram News Bot

This is a Telegram bot for receiving and managing news.

## Prerequisites

* Python 3.11 or higher
* A bot token from [@BotFather](https://t.me/BotFather)
* You can get your ID from [@userinfobot](https://t.me/userinfobot)
* Open the config.json file and change the AI ​​prompt, topics, and news site links if needed.


## Setup (Linux and Windows)

1. Clone the repository and go to the folder:
```bash
git clone https://github.com/amirehp/telegram_news_bot.git
cd telegram_news_bot
```

2. Create and activate a virtual environment:
```bash
# in linux:
python3 -m venv .venv
source .venv/bin/activate

# in windows:
python -m venv .venv
.venv\Scripts\activate
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Create a file named `.env` in the root of the project and put the following values ​​in it:
```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
TELEGRAM_OWNER_ID=your_telegram_user_id_here
GEMINI_API_KEY=your_gemini_api_key
```
To get the gemini API key:
https://aistudio.google.com/app/api-keys


## run the bot

To run manually:

on windows:
```bash
python src/main.py
```

or on linux:
```bash
python3 src/main.py
```

## Automatic execution
### in linux (Systemd)

To automatically run the bot on Ubuntu/Linux, use a `service` file:

1. Make the executable file executable
`chmod +x path/to/project/run.sh`


2. Create a service file: `sudo nano ~/.config/systemd/user/newsbot.service`
3. Put the following content in it (correct the paths):
```ini
[Unit]
Description=AI News Telegram Bot

[Service]
Type=oneshot
WorkingDirectory=/path/to/project
ExecStart=/path/to/project/.venv/bin/python src/main.py
```

4. create a Timer
`nano ~/.config/systemd/user/newsbot.timer`

5. write these in the file. ( set your desired period instead of 1 hour )
```ini 
[Unit]
Description=Run AI News Telegram Bot every hour

[Timer]
OnBootSec=10min
OnUnitActiveSec=1h

[Install]
WantedBy=timers.target
```

6. Enable and run the service:
```bash
systemctl --user daemon-reload
systemctl --user enable --now newsbot.timer 
```

### in windows (Task Scheduler) 

1. Run the following command in CMD (with Administrator access):

```cmd
schtasks /create /tn "NewsBot" /tr "\"C:\path\to\your\project\run.bat\"" /sc onlogon /rl highest
```

2. To set the repetition (for example, every 2 hours), open `Task Scheduler` (with the `taskschd.msc` command) and in the robot's `Trigger` settings, check `Repeat task every` to `2 hours` and `Duration` to `Indefinitely`.

Task Scheduler →  task NewsBot → Properties → Triggers → Edit → Repeat task every: 2 hours → Duration: Indefinitely.

Restart the system once and it should work automatically at the time you specified.
Of course, I didn't realize that I changed other settings on Windows because it didn't work properly at first.

## contribution

I would be happy if you have a suggestion, please submit it as an Issue or Pull Request.




