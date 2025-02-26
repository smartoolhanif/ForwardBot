import os

class Config:
    API_ID = os.environ.get("API_ID", "28580773")
    API_HASH = os.environ.get("API_HASH", "f80e465a8805bee5c6bf29fa12d6cc0c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7794943135:AAG3U8Cu9U3I4EZOGu4WA_o-oToQSHNmYnU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://telegrambott19:telegrambott19@cluster0.hetez.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
