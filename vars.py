

from os import environ

API_ID = int(environ.get("API_ID", "33642705"))
API_HASH = environ.get("API_HASH", "e6f71b5d10d8a5482990f4c9add0b1ea")
BOT_TOKEN = environ.get("BOT_TOKEN", "8928906721:AAETgxbiUTlz_bZQVMBmdtmMKxs9tyVrvJI")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "roxybasicneedbot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/roxybasicneedbot1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")




