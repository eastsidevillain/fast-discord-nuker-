#made by rockstar#0002

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


apiv = [6, 7, 8, 9]


def http_requests(members):
    try:
        http = httplib2.Http()
        http.request(
            "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                random.choice(apiv), guild, members, time.sleep(0.100)
            ),
            method="PUT",
            headers={"Authorization": f"Bot {token}"},
        )
    except Exception:
        print("Error [!] -> Having Trouble Sending Requests ")


if __name__ == "__main__":

    threads = []

    with ThreadPoolExecutor() as executor:

        for m in members:
            threads.append(executor.submit(http_requests, m))

            print(
                f"{Fore.CYAN}{Style.BRIGHT}{Style.DIM} Succesfully Punished User -> ; {Fore.RESET}  "
                + m
            )
