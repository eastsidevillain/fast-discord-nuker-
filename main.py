# dont skid

from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import os, random

os.system("cls & mode 80, 23")
token, guild = input("TOKEN: "), input("GUILD: ")
members = open("members.txt")
os.system("cls & mode 80, 23")



def mass_ban(members):
    try:
        session = FuturesSession()
        (session.put(
                "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                    random.randint(6, 9), guild, members
                ),
                headers={"Authorization": f"Bot {token}"},
            ),
        )
    except:
        return


if __name__ == "__main__":
    threads = []

    with ThreadPoolExecutor(max_workers=110) as executor:

        for m in members:

            threads.append(executor.submit(mass_ban, m))
        try:
            print(f'Succesfully Banned; ' + m)

        except:

            print(f'Unable To Ban;' + m + '[RATELIMITED]')
