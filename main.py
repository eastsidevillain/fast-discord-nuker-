try:

    from concurrent.futures import ThreadPoolExecutor
    from colorama import Style, Fore
    import os, httplib2, random, time

except Exception:
    print("Error -> Missing Modules Please Install them.")

os.system("cls & mode 80, 23")


token, guild = (
    input("Token -> "),
    input("Guild ID -> "),
)

with open("members.txt") as f:
    members = f.readlines()


def http_requests(members):
    try:
        http = httplib2.Http()
        http.request(
            "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                random.randint(6, 9), guild, members, time.sleep(0.100)
            ),
            headers={"Authorization": f"Bot {token}"},
        )
    except:
        pass


if __name__ == "__main__":

    threads = []

    with ThreadPoolExecutor() as executor:

        for m in members:
            threads.append(executor.submit(http_requests, m))

            print(
                f"{Fore.CYAN}{Style.BRIGHT}{Style.DIM} Punished User -> ; {Fore.RESET}  "
                + m
            )
