import ctypes
import json
import os
import queue
import random
import threading
import time

import colorama
import requests
from colorama import *
from discord_webhook import DiscordEmbed, DiscordWebhook

os.system('cls')
usernames = queue.Queue()
p_pr = queue.Queue()


usersize = usernames.qsize()
psize = p_pr.qsize()

target = input(f'[{Fore.GREEN}Input{Fore.WHITE}] Target: ')
ssid = input(f'[{Fore.GREEN}Input{Fore.WHITE}] Session Id: ')
threads = int(input(f'[{Fore.GREEN}Input{Fore.WHITE}] Threads: '))
p_file = input(f"[{Fore.GREEN}Input{Fore.WHITE}] Proxy File:  ")
wh = input(f"[{Fore.GREEN}Input{Fore.WHITE}] Webhook:  ")
a = 0


class Main:

    def init(self):
        self.rl = 0
        self.attetmps = 0
        self.er = 0
        self.claimed = False
        self.multi_sessions = False
        self.see_stats = False

    def Swapper(self):
        global a

        urlsw = 'https://api22-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7036235088292595462&device_id=7029768732902278661&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220105&version_name=22.1.5&device_platform=android&ab_version=22.1.5&ssmix=a&device_type=A5010&device_brand=OnePlus&language=en&os_api=25&os_version=7.1.2&openudid=855e35166e818944&manifest_version_code=2022201050&resolution=720*1280&dpi=240&update_version_code=2022201050&_rticket=1638582241585&current_region=US&app_type=normal&sys_region=US&mcc_mnc=31610&timezone_name=Asia%2FShanghai&residence=US&ts=1638582240&timezone_offset=28800&build_number=22.1.5&region=US&uoo=0&app_language=en&carrier_region=US&locale=en&op_region=US&ac2=wifi&cdid=7891595b-0003-42e9-a15d-f512d5bb9fa9&support_webview=1&okhttp_version=4.0.69.4-tiktok'
        for line in open(p_file, 'r'):
            p_pr.put(line.strip())

        self.head = {
            'accept-encoding': 'gzip',
            'connection': 'Keep-Alive',
            'content-length': '63',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': f'sessionid={ssid}',
            'host': 'api22-normal-c-useast1a.tiktokv.com',
            'multi_login': '1',
            'passport-sdk-version': '19',
            'sdk-version': '2',
            'user-agent': 'com.zhiliaoapp.musically/2022201050 (Linux; U; Android 7.1.2; en_US; A5010; Build/N2G48H;tt-ok/3.10.0.2)',
        }
        while True:
            a += 1
            p = p_pr.get()
            self.Proxies = {
                "http": f'http://{p}',
                "https": f'https://{p}'
            }

            self.proxy_rotate = random.choice(self.Proxies)

            r = requests.post(urlsw, headers=self.head,
                              proxies=self.proxy_rotate, data=f'login_name={target}').text

            if 'success' in r:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Claimed {Fore.GREEN}@{target}')
                ctypes.windll.user32.MessageBoxW(
                    0, f'claimed {target}', f'attempts : {a}', 1)
                webhook = DiscordWebhook(url=wh)
                embed = DiscordEmbed(title=f'Soul Has Claimed a username | https://tiktok.com/@%7Btarget%7D',
                                     description=f' User: {target} Attetmps: {a}| \n json: {r}', color='03b2f8')
                webhook.add_embed(embed)
                response = webhook.execute()
                input(f'press input to exit...')
                quit()
            else:
                a += 1


t = Main()

thread = []
for i in range(threads):
    t = threading.Thread(target=t.Swapper())
    t.daemon = True
    t.start()
    thread.append(t)
for threads in thread:
    threads.join()
