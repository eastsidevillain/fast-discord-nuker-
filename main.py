# dont skid

from concurrent.futures import ThreadPoolExecutor, as_completed
from requests_futures.sessions import FuturesSession
import queue, os, random, concurrent.futures

os.system("cls & mode 80, 23")
token, guild = input("TOKEN: "), input("GUILD: ")

members = open("members.txt")

os.system("cls & mode 80, 23")


os.system(f"cls & mode 70, 25 & title Executed Mass Ban")
q = queue.Queue()


def mass_ban(members):
    try:
        session = FuturesSession()
        q.put(
            session.put(
                "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                    random.randint(6, 9), guild, members
                ),
                headers={"Authorization": f"Bot {token}"},
            ),
        )
        q.join()
    except:
        return


if __name__ == "__main__":
    
    threads = []
    
    with ThreadPoolExecutor(max_workers=110) as executor:
    
        for m in members:
            
            threads.append(executor.submit(mass_ban, m))
