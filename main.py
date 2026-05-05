import os
import json
import requests
import socket
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def banner():
    print("\033[32m")
    print(r"""
 ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

                                    ─────── OSINT TOOLKIT ───────""")
    print("\033[0m")


def check_username(site, url, username):
    try:
        full_url = url.format(username)
        res = requests.get(full_url, timeout=5)

        if res.status_code == 200 and "not found" not in res.text.lower():
            return (site, full_url, True)
        else:
            return (site, full_url, False)

    except:
        return (site, url.format(username), False)


def username_search():
    username = input("\nEnter username: ")

    with open("sites.json") as f:
        sites = json.load(f)

    print(f"\nSearching for '{username}'...\n")

    results = []

    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [
            executor.submit(check_username, site, url, username)
            for site, url in sites.items()
        ]

        for future in futures:
            results.append(future.result())

    for site, url, found in results:
        if found:
            print(f"\033[32m[+] FOUND on {site}: {url}\033[0m")
        else:
            print(f"\033[31m[-] Not found on {site}\033[0m")


def instagram_lookup():
    user = input("\nEnter Instagram username: ")

    url = f"https://www.instagram.com/{user}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print("Failed to fetch profile")
        return

    if '"username"' not in res.text:
        print("User not found or blocked")
        return

    print("\n[+] Profile exists")
    print(f"[+] Profile URL: {url}")


def domain_lookup():
    domain = input("\nEnter domain: ")

    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Domain: {domain}")
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Could not resolve domain")


def menu():
    while True:
        print("""
\033[91m[1]\033[91m\033[93m.\033[93m \033[91mUsername Search\033[91m
\033[91m[2]\033[91m\033[93m.\033[93m \033[91mInstagram Check\033[91m
\033[91m[3]\033[91m\033[93m.\033[93m \033[91mDomain Lookup\033[91m
\033[91m[4]\033[91m\033[93m.\033[93mExit
""")

        choice = input("Select option : ")

        if choice == "1":
            username_search()
        elif choice == "2":
            instagram_lookup()
        elif choice == "3":
            domain_lookup()
        elif choice == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    os.system("clear")
    banner()
    menu()