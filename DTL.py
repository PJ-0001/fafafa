import requests
import time
import os
from colorama import Fore
import subprocess
import platform


def run_another_script(script_path):
    if platform.system() == "Windows":
        subprocess.call(["python", script_path], shell=True)
    else:
        subprocess.call(["python3", script_path])


# Used for the Subprocess packet and executes it in the command/shell
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error executing command: {command}")


# Clear cls or clear in Linux using the subprocess packet
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def banner():
    print(Fore.LIGHTRED_EX + '''\
$$$$$$$\            $$$$$$$\         $$$$$$\  $$\                           $$\ 
$$  __$$\           $$ __$$\       $$  __$$\ $$ |                          $$ |
$$ |  $$ |$$\   $$\ $$ |  $$ |      $$ /  \__|$$ | $$$$$$\  $$\   $$\  $$$$$$$ |
$$$$$$$  |\$$\ $$  |$$ |  $$ |      $$ |      $$ |$$  __$$\ $$ |  $$ |$$  __$$ |
$$  ____/  \$$$$  / $$ |  $$ |      $$ |      $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |
$$ |       $$  $$<  $$ |  $$ |      $$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |      $$  /\$$\ $$$$$$$  |      \$$$$$$  |$$ |\$$$$$$  |\$$$$$$  |\$$$$$$$ |
\__|      \__/  \__|\_______/        \______/ \__| \______/  \______/  \_______|
                                                                                                                                
    ''')


def send_discord_message(username, url):
    webhook_url = "https://discord.com/api/webhooks/1135209141724520468/8kNIh0OXYzclA6SYGkWAF1_8SU2piH9nodRbfzlyQ2iC-xPTEvA-3nPPmeFXq0AcViEf"
    message = f'@everyone Found information for username: {username}\nURL: {url}'

    data = {
        "content": message
    }

    response = requests.post(webhook_url, json=data)
    response.raise_for_status()


def search():
    time.sleep(0.5)
    print(Fore.LIGHTRED_EX + f'[🤡] Zoeken op gebruikersnaam: {username}')
    time.sleep(0.5)
    print('████████')

    time.sleep(0.5)

    print('████████\n')
    time.sleep(0.5)

    print(Fore.LIGHTMAGENTA_EX + "[+] PxD Dox is bezig ")

    time.sleep(0.5)

    print('████████')

    time.sleep(0.5)

    print('████████\n')

    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        try:
            r = requests.get(url, verify=True)  # Disable SSL certificate verification
            r.raise_for_status()

            if r.status_code == 200:
                if match:
                    print(Fore.LIGHTYELLOW_EX + '[+] Resultaten')
                    match = False
                print(Fore.LIGHTYELLOW_EX + f'\n{url} - {r.status_code} - OK')
                if username in r.text:
                    print(Fore.LIGHTGREEN_EX + f'[PXD-Dox] POSITIEF: Gebruikersnaam: {username} - Deze gebruikersnaam is gevonden op deze URL')
                    send_discord_message(username, url)  # Send the found info to Discord webhook
                else:
                    print(Fore.LIGHTRED_EX + f'[PXD-Dox] NEGATIEF: Gebruikersnaam: {username} - Deze gebruikersnaam is niet gevonden op deze URL, MOGELIJK FOUT-NEGATIEF.')
        except requests.exceptions.RequestException as e:
            print(Fore.LIGHTRED_EX + f'[ERROR] Kon geen verbinding maken met URL: {url}')
            print(Fore.LIGHTRED_EX + f'[ERROR] {e}')
        count += 1

    total = len(WEBSITES)
    print(Fore.WHITE_EX + f'AFGEROND: Met een totaal van {count} gevonden accounts op {total} websites.')
    script_path = "main.py"
    run_another_script(script_path)


if __name__ == '__main__':
    banner()

    ''' GEEF DE GEBRUIKERSNAAM VAN DE PERSOON DIE JE WILT DOXEREN :) '''
    username = input(Fore.LIGHTGREEN_EX + '{+} Voer de gebruikersnaam in: ')

    # Lijst met websites om de gebruikersnaam te zoeken
    WEBSITES = [
        f'https://www.instagram.com/{username}',
        f'https://www.facebook.com/{username}',
        f'https://www.twitter.com/{username}',
        f'https://www.youtube.com/{username}',
        f'https://{username}.blogspot.com',
        f'https://plus.google.com/s/{username}/top',
        f'https://www.reddit.com/user/{username}',
        f'https://{username}.wordpress.com',
        f'https://www.pinterest.com/{username}',
        f'https://www.github.com/{username}',
        f'https://{username}.tumblr.com',
        f'https://www.flickr.com/people/{username}',
        f'https://steamcommunity.com/id/{username}',
        f'https://vimeo.com/{username}',
        f'https://soundcloud.com/{username}',
        f'https://disqus.com/by/{username}',
        f'https://medium.com/@{username}',
        f'https://{username}.deviantart.com',
        f'https://vk.com/{username}',
        f'https://about.me/{username}',
        f'https://imgur.com/user/{username}',
        f'https://flipboard.com/@{username}',
        f'https://slideshare.net/{username}',
        f'https://fotolog.com/{username}',
        f'https://open.spotify.com/user/{username}',
        f'https://www.mixcloud.com/{username}',
        f'https://www.scribd.com/{username}',
        f'https://www.badoo.com/en/{username}',
        f'https://www.patreon.com/{username}',
        f'https://bitbucket.org/{username}',
        f'https://www.dailymotion.com/{username}',
        f'https://www.etsy.com/shop/{username}',
        f'https://cash.me/{username}',
        f'https://www.tiktok.com/@{username}',
        f'https://www.behance.net/{username}',
        f'https://www.goodreads.com/{username}',
        f'https://www.instructables.com/member/{username}',
        f'https://keybase.io/{username}',
        f'https://kongregate.com/accounts/{username}',
        f'https://{username}.livejournal.com',
        f'https://angel.co/{username}',
        f'https://last.fm/user/{username}',
        f'https://dribbble.com/{username}',
        f'https://www.codecademy.com/{username}',
        f'https://en.gravatar.com/{username}',
        f'https://pastebin.com/u/{username}',
        f'https://foursquare.com/{username}',
        f'https://www.roblox.com/user.aspx?username={username}',
        f'https://www.gumroad.com/{username}',
        f'https://{username}.newgrounds.com',
        f'https://www.wattpad.com/user/{username}',
        f'https://www.canva.com/{username}',
        f'https://creativemarket.com/{username}',
        f'https://www.instagram.com/{username}',
        f'https://www.snapchat.com/add/{username}'

    ]

    search()
