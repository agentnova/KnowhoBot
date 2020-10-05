import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class cred():

    BOT_TOKEN = os.getenv("1337673070:AAGu_qNlGDxgNaY-3QIodqHh9snKLSkhp30") #From botfather

    API_ID = os.getenv("1144902")       #"Get this value from my.telegram.org! Please do not steal"

    API_HASH = os.getenv("e743e5a4f35076e4c558a4bd713082e9")   #"Get this value from my.telegram.org! Please do not steal"

    DB_URL = os.getenv("https://truecalerbot.firebaseio.com/")       #From Firebase database

    ####From Truecaller and Eyecon app request headers respectively########

    T_AUTH = os.getenv("Bearer a1i0u--NIp2_MFJVY8O7bRbZZOQjxTNCtLkWddGx67BwRP5UqX_L41Vc05bNqf1d")      # Truecaller auth id CA

    E_AUTH = os.getenv("93a4faee-9a6d-4908-90e9-8ebb85deddbe")      # Eyecon auth id

    E_AUTH_V=os.getenv("e1")    # Eyecon auth_v

    E_AUTH_C=os.getenv("39")    # Eyecon auth_c
