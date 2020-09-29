# KnowhoBot

Pluggable
[Telegram](https://telegram.org) bot based on
[Pyrogram](https://github.com/pyrogram/pyrogram).


This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
Mozilla Public License for more details.

### Installation

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/agentnova/KnowhoBot)



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
#### Edit the creds.py with your own variables as given below
```python3
class cred():
    BOT_TOKEN = "your bot token from botfather"
    API_ID = "your api id from my.telegram.org!"       
    API_HASH = "your api hash from my.telegram.org!"   
    DB_URL = "your database url from google firebase"      

    ####From Truecaller and Eyecon app request headers respectively########

    T_AUTH = "from telegram app request header"     
    E_AUTH = "from eyecon app request header"     
    E_AUTH_V= "from eyecon app request header"    
    E_AUTH_C= "from eyecon app request header" 
    
```
