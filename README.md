# KnowhoBot

Pluggable
[Telegram](https://telegram.org) bot based on
[Pyrogram](https://github.com/pyrogram/pyrogram).

## About the bot

>Simply the purpose of this bot is to gather information about a phone number(only indian numbers).

>Combined Results from Truecaller and eyecon app is provided.

>Saves your time...:-)

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
Mozilla Public License for more details.

### Installation

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/agentnova/KnowhoBot)

#### Watch video

<a href="https://youtu.be/n3OAebcVgR4"><img src="https://github.com/agentnova/KnowhoBot/blob/master/images%20(1)%7E2.jpg" width="150px"/></a>



#### The Legacy Way
Simply clone the repository and run the main file:
```sh
git clone https://github.com/agentnova/KnowhoBot.git

cd KnowhoBot

python3 -m venv venv

. ./venv/bin/activate

pip install -r requirements.txt

python3 main.py

```
#### Dont forget to edit the creds.py with your own variables like below with your own values
```python3
class cred():
    BOT_TOKEN = "your bot token from botfather"
    API_ID = "your api id from my.telegram.org!"       
    API_HASH = "your api hash from my.telegram.org!"   
    DB_URL = "your database url from google firebase"      
    T_AUTH = "from telegram app request header"     
    E_AUTH = "from eyecon app request header"     
    E_AUTH_V= "from eyecon app request header"    
    E_AUTH_C= "from eyecon app request header" 
    
```

