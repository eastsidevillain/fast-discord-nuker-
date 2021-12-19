import discord, os
from discord.ext import commands

os.system("cls & mode 80, 23")
f = open("members.txt", "w")
f.close()


TOKEN = input(f"BOT TOKEN -> ")
os.system("cls & mode 80, 23")

intents = discord.Intents.all()
client = commands.Bot(command_prefix=None, intents=intents)


@client.event
async def on_ready():
    print(f"Connected to -> {client.user}.")
    GUILD = int(input("\nGuild ID to Scrape -> "))
    os.system("cls")
    id = client.get_guild(GUILD)
    y = open("members.txt", "a")
    for member in id.members:
        y.write(f"\n{member.id}")
    print(f"Succesfully Scraped Members")


client.run(TOKEN, bot=True)
