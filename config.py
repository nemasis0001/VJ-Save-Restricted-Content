import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28348410"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f6db276c339d8c900ecb2fb588128ede")

# Your Owner / Admin Id For Broadcast (Supports Multiple Admins)
ADMINS = list(map(int, os.environ.get("ADMINS", "6073523936").split()))

# Your Mongodb Database Url
DB_URI = os.environ.get(
    "DB_URI", 
    "mongodb+srv://adityanegi735:SQlQhAOLyAbVaE32@cluster0.ig6gv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Your Database Name
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then False
ERROR_MESSAGE = os.environ.get('ERROR_MESSAGE', 'True').lower() == 'true'
