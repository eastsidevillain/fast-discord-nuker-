# made by rockstar#0002

from concurrent.futures import ThreadPoolExecutor
from colorama import Style, Fore
import os, httplib2, random, time

os.system("cls & mode 80, 23 & title OMEN")


with open("members.txt") as f:
    members = f.readlines()

apiv = [6, 7, 8, 9]  # api versions to randomize by


def http_requests(members):
    try:
        h = httplib2.Http()
        h.request(
            "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                random.choice(apiv), guild, members, time.sleep(0.100)
            ),
            method="PUT",
            headers={"Authorization": f"Bot {token}"},
        )

    except:
        pass


if __name__ == "__main__":
    token, guild = input(f"TOKEN -> "), input(f"GUILD -> ")
    os.system("cls & mode 80, 23 & title Mass Ban Executed - Omen")

    threads = []

    with ThreadPoolExecutor() as executor:

        for m in members:
            threads.append(executor.submit(http_requests, m))

            print(
                f"{Fore.CYAN}{Style.BRIGHT}{Style.DIM} Succesfully Punished User -> ; {Fore.RESET}  "
                + m
            )
