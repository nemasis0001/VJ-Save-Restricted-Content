import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28348410"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f6db276c339d8c900ecb2fb588128ede")


# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get(
    "DB_URI", 
    "mongodb+srv://adityanegi735:your_real_password@cluster0.ig6gv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
