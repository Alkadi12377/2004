from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "5610203320:AAHj8y4shFqR1FKA0DRwRkRoH5XbunviVmY")
SESSION_NAME = getenv("SESSION_NAME", "BAAWcYtkLPVELPasCWqyWQDavNS3TM6EFa9LLVLHJ6hCzG72jousRjpjqMZgC3__Am_I4Fszny3136oDeR09WlEEkBxqXfQhFpof10pDVxnlRHRz8snts0AqU6iU39kiufyq7VcduC7TiJILONEnqrbo7L7eNrp_4vU2QlhfXLvBjiPVfb6LQJiA_2Jn4IaNmp-tXl15IkDNMZNIHsMfvGOHqsW1SoS1eRwRWClbLVeiVz0l0p-sKig5zmGSs24iVekC2LsSyY4ws2I72hIO-_n7xY5j4ydoGGCugG5nkIePz5UeQ2tZMleuGrXBUdYL2hczZ7-igQjIp4Djsntws5p8AAAAAW7QGtsA)

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "o1_1m")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Alsjzj99bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
