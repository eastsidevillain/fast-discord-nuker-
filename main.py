from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import os, random
from colorama import Style, Fore


c = Fore.RESET
os.system("cls & mode 80, 23 & title PHOBOS!")
token, guild = input("TOKEN: "), input("GUILD: ")

with open("members.txt") as f:
    members = f.readlines()


def mass_ban(members):
    try:
        session = FuturesSession()
        (
            session.put(
                "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                    random.randint(6, 9), guild, members
                ),
                headers={"Authorization": "Bot" + token},
            ),
        )
    except:
        return


if __name__ == "__main__":
    threads = []

    with ThreadPoolExecutor() as executor:

        for m in members:

            threads.append(executor.submit(mass_ban, m))

            print(
                f"{Fore.CYAN}{Style.BRIGHT}{Style.DIM}Succesfully Banned -> ; {c} " + m
            )
