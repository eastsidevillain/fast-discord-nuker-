from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
from colorama import Style, Fore
import os, httplib2


os.system(" cls & mode 80, 23 & title PHOBOS! ")


with open("members.txt") as f:
    members = f.readlines()


def mass_ban_users(members):
    try:
        h = httplib2.Http(".cache")
        h.request(
            f"https://discord.com/api/v9/guilds/{guild}/bans/{members}",
            method="PUT",
            headers={"Authorization": f"Bot {token}"},
        ),
    except:
        return


if __name__ == "__main__":
    token, guild = input("TOKEN ; "), input("GUILD ; ")
    threads = []
    with ThreadPoolExecutor() as executor:

        for m in members:

            threads.append(executor.submit(mass_ban_users, m))

            print(
                f"{Fore.CYAN}{Style.BRIGHT}{Style.DIM} Succesfully Punished User -> ; {Fore.RESET}  "
                + m
            )
