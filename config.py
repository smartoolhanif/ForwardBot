import os

class Config:
    API_ID = os.environ.get("API_ID", "10253517")
    API_HASH = os.environ.get("API_HASH", "65222e5b2950c2a486ac61964123b83a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7722659903:AAE7FvrveuF0UTetvMa1SF-2UKGnsrjgzE4") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "viewboosterhanif_bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://ckinghanif:l5jY7NXB9kELEHlQ@cluster0.halfsnx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '5260441331').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
