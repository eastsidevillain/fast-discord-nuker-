try:
    from concurrent.futures import ThreadPoolExecutor
    from requests_futures.sessions import FuturesSession
    import random, time, os
    from colorama import Fore, Style
except ImportError:
    print("Error [!] -> Modules Are not installed")


os.system("cls & mode 80, 23")

token, guild = (input("Token -> "), input("Guild ID -> "))

threads = []
apiv = [6, 7, 8, 9]
codes = [200, 201, 204]

os.system("cls & mode 80, 23")


def worker(user: str):
    try:
        session = FuturesSession()
        response = session.put(
            "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                random.choice(apiv), guild, user, time.sleep(0.050)
            ),
            headers={"Authorization": "Bot {}".format(token)},
        ).result()
        if response.status_code in codes:
            print(
                f"{Fore.CYAN}{Style.BRIGHT} Succesfully Punished Member -> {Fore.RESET}"
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
    while True:
        theadpool()
