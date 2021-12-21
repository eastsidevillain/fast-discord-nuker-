try:

    from concurrent.futures import ThreadPoolExecutor
    from colorama import Style, Fore
    import os, httpx, random, time

except Exception:
    print("Error -> Missing Modules Please Install them.")

os.system("cls & mode 80, 23")


token, guild = (
    input("Token -> "),
    input("Guild ID -> "),
)

with open("members.txt") as f:
    members = f.readlines()


apivs = [6, 7, 8, 9]


def http_requests(members):
    response = httpx.put(
        "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
            random.choice(apivs), guild, members, time.sleep(0.100)
        ),
        headers={"Authorization": f"Bot {token}"},
    )

    if (
        response.status_code == 200
        or response.status_code == 201
        or response.status_code == 204
    ):
        print(
            f"""             {Fore.CYAN}{Style.DIM} Succesfully Punished -> ; {Fore.RESET}"""
            + members
        )


if __name__ == "__main__":

    threads = []

    with ThreadPoolExecutor() as executor:
        

        for m in members:
            
            
            threads.append(executor.submit(http_requests, m))
