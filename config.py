from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2598fb4de9716f0fa8999.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/6b9411602aa17ac3ac529.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/S_MA4")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/S_MA4")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2095495680").split()))


FAILED = "https://telegra.ph/file/a6d6c05349501e55b004d.jpg"
