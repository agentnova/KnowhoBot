import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred():
    BOT_TOKEN = os.getenv("BOT_TOKEN") #From botfather
    API_ID = os.getenv("API_ID")       #"Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv("API_HASH")   #"Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("DB_URL")       #From Firebase database

    ####From Truecaller and Eyecon app request headers respectively########

    T_AUTH = os.getenv("T_AUTH")      # Truecaller auth id CA
    E_AUTH = os.getenv("E_AUTH")      # Eyecon auth id
    E_AUTH_V=os.getenv("E_AUTH_V")    # Eyecon auth_v
    E_AUTH_C=os.getenv("E_AUTH_C")    # Eyecon auth_c
