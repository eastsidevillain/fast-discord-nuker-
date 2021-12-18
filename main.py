# made by rockstar#0002
# give me credits if u want to skid
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
        (
            h.request(
                "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                    random.choice(apiv),
                    guild,
                    members,
                    time.sleep(
                        0.100
                    ),  # delayed the http requests sent by 0.100 seconds/KEEP THIS AT 0.100 DONT CHANGE
                ),
                method="PUT",
                headers={"Authorization": f"Bot {token}"},
            ),
        )

        print(
            f"{Fore.CYAN}{Style.DIM} Succesfully Punished User -> ; {Fore.RESET} " + m
        )
    except:

        pass


if __name__ == "__main__":
    token, guild = input("TOKEN ; "), input("GUILD ; ")
    threads = []

    with ThreadPoolExecutor() as executor:

        for m in members:

            threads.append(executor.submit(http_requests, m))
