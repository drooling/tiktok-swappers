import ctypes
import os
import socket
import threading
import time

import colorama
import requests
from colorama import Fore

colorama.init(autoreset=colorama)
Attempt = 0
NoSpam = 0
ip = "hi"
headers_verify = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-encoding': 'gzip, deflate, br',
                  'accept-languagrole': 'en-US,en;q=0.9',
                  'cache-cont': 'no-cache',
                  'cookie': '_pbjs_userid_consent_data=3524755945110770; _ga_0DTZ6LRDBJ=GS1.1.1620136816.4.1.1620136838.37; _ga=GA1.2.1901645475.1617284914; __gads=ID=1ca5438212d4d9de:T=1624630836:S=ALNI_MaG4g2aXDmjXeUIX2ZOUvSX5D8nKw; _gid=GA1.2.643533148.1629376559; SKpbjs-unifiedid=%7B%22TDID%22%3A%22bb8cb9ee-3bd0-46d7-b9bd-2deb7fd990e6%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222021-07-19T12%3A51%3A32%22%7D; _identity-frontend=65ce165faaff14e66d9b586e5f198c1711428f2e0b2466cae5f25edefa679aada%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A53%3A%22%5B7602843%2C%22NeMMLKvGPTV-tR4uPHAJRV2WhIN1OH0j%22%2C15552000%5D%22%3B%7D; cf_clearance=0fpIzGmaK4Evkl0ghRhbDVXu2XfbrXsxGPChL7BSEEA-1629421201-0-250; pastebin-frontend=323e45d76aa3a7ef5c07872872694050; _csrf-frontend=f50e72016e28a46ffdd94a510b85aec5f03166a735d14a7d2ed8afc75d578239a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22McCZvxh_AXe5tSZPpz19cI9vJl_gV1EY%22%3B%7D; _gat_gtag_UA_58643_34=1; SKpbjs-id5id=%7B%22created_at%22%3A%222021-07-31T17%3A07%3A57Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOYACljRE_jjpU159ON6Jixjl8-Wv19z3P6H0ZrQ!ID5*xWQr9P8swzaOE-iBy_v59aiOBH2mUJ_QattbdHdRfxYAAJiIUaWMeZrvmnR-p_U1%22%2C%22universal_uid%22%3A%22ID5-ZHMO7b1wQPmpih9jH29zsQsxYeiQwS3KsuwEcipzRQ!ID5*a84lA9w7GAzIL-JTUpkHP4CNWS3ZFqlh-zSESEOsGwkAAGtVhoZjxNncn-gYtNTw%22%2C%22signature%22%3A%22ID5_AfCHBnf4Ytj860LzoEDnqBA0Y7q15ppTmimBT21399XUmD0k7m09ikSPRyMaeQFWYGwI9QRevNdEV6U6KEUFgVA%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%2C%22privacy%22%3A%7B%22jurisdiction%22%3A%22other%22%2C%22id5_consent%22%3Atrue%7D%7D; SKpbjs-id5id_last=Fri%2C%2020%20Aug%202021%2018%3A16%3A29%20GMT; cto_bidid=_0AcXl9McnVtc0VodzUxakhUanhwVEVzZUtpV2pVTTN3V3I4UVR6SkpodUlVZnl5WGJlR2FRSHhpdVlkSmlzSlc1WHJ6Z1UwYkVBT3RiJTJGTiUyRlBzMHQzdUJEaDh1RnBlNWp4bnlRdGd1bXh1Y21TVjAlM0Q; cto_bundle=cj4XqV85clBQTmx5VFBQa2xmNHZidXJ1aktDdiUyQlVJRjlsSlYzdTB1QTBFSE9BNm1yTVdaeFVoWTlOTmh6JTJGOHdtb0hEJTJCb3BFUUZEUEtFTEZkQkUxaWtCaWtucTlBR2h5dVVmS1lpRGJnZzZLY0RaTFdQdTZMU2olMkJqJTJGYkRpJTJCZDZHSWgwblI1YkxjSHpwNVk0MUhGVXQ4V3BPdEElM0QlM0Q; SKpbjs-unifiedid_last=Fri%2C%2020%20Aug%202021%2018%3A16%3A30%20GMT; _gat_gtag_UA_128776493_31=1; __viCookieActive=true',
                  'pragma': 'no-cache',
                  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
req_verify = "hi"
MessageBox = ctypes.windll.user32.MessageBoxW
if ip in req_verify:
    try:
        def start():
            NameBanner = ("tik")
            req_banner = requests.get(
                f"http://artii.herokuapp.com/make?text={NameBanner}").text
            print(req_banner)
            sessionid = input('[-] Sessionid : ')
            username = input('[-] Target : ')
            Thread = int(input('[-] Thread : '))
            Attempt = 0
            MessageBox = ctypes.windll.user32.MessageBoxW

            def check_sessionid():
                url_check_sessionid = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                headers_check_sessionid = {'Host': 'api2-t2.musical.ly',
                                           'Connection': 'close',
                                           'Content-Length': '655',
                                           'Accept-Encoding': 'gzip, deflate',
                                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                           'User-Agent': 'com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'}
                data_check_sessionid = 'unique_id=ff'
                cookies_check_sessionid = {'sessionid': sessionid}
                req_check_sessionid = requests.post(
                    url_check_sessionid, headers=headers_check_sessionid, data=data_check_sessionid, cookies=cookies_check_sessionid)
                casesaesa = req_check_sessionid.text
                print(casesaesa)
                print(req_check_sessionid.status_code)
                if '"status_code": 2091' in casesaesa:
                    os.system('cls')
                    print(req_banner)
                    print(f"[-] Sessionid : {sessionid}")
                    print(f"[-] Target : {username}")
                    print(f"[-] Thread : {Thread}")
                    print(
                        f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Login" + Fore.RESET)
                    time.sleep(2)

                    def set_nickname():
                        global nickname
                        url_set_nickname = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                        headers_set_nickname = {'Host': 'api2-t2.musical.ly',
                                                'Connection': 'close',
                                                'Content-Length': '655',
                                                'Accept-Encoding': 'gzip, deflate',
                                                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                                'User-Agent': 'com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'}
                        data_set_nickname = f"nickname=kettle"
                        cookies_set_nickname = {'sessionid': sessionid}
                        req_set_nickname = requests.post(
                            url_set_nickname, headers=headers_set_nickname, data=data_set_nickname, cookies=cookies_set_nickname).text
                        if '"status_code": 0' in req_set_nickname:
                            print(
                                f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Set Nickname {Fore.RESET}To {Fore.LIGHTYELLOW_EX}kerrle" + Fore.RESET)
                            time.sleep(2)

                            def set_bio():
                                global Bio
                                url_change_bio = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                                headers_change_bio = {'Host': 'api2-t2.musical.ly',
                                                      'Accept': '*/*',
                                                      'Content-Type': 'application/x-www-form-urlencoded',
                                                      'Accept-Encoding': 'gzip, deflate',
                                                      'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
                                                      'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
                                                      'Content-Length': '19',
                                                      'Connection': 'close'}
                                cookies_change_bio = {'sessionid': sessionid}
                                data_change_bio = f"signature=kerrle swap"
                                response_change_bio = requests.post(
                                    url_change_bio, data=data_change_bio, cookies=cookies_change_bio, headers=headers_change_bio).text
                                if '"status_code": 0' in response_change_bio:
                                    print(
                                        f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Set Bio {Fore.RESET}To {Fore.LIGHTYELLOW_EX}kerrle swap" + Fore.RESET)

                                    def check():
                                        global Attempt
                                        global NoSpam
                                        url = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                                        headers = {'Host': 'api2-t2.musical.ly',
                                                   'Connection': 'close',
                                                   'Content-Length': '655',
                                                   'Accept-Encoding': 'gzip, deflate',
                                                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                                   'User-Agent': 'com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'}
                                        data = f"unique_id={username}"
                                        cookies = {'sessionid': sessionid}
                                        while True:
                                            req = requests.post(
                                                url, headers=headers, data=data, cookies=cookies).text
                                            if 'unique_id' in req:
                                                if NoSpam == 0:
                                                    NoSpam = 1
                                                    os.system('cls')
                                                    print(req_banner)
                                                    print(
                                                        f"[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] All threads successfully initialized")
                                                    print(
                                                        f"[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] Swapped username {Fore.LIGHTGREEN_EX}@{username} {Fore.RESET}after{Fore.LIGHTGREEN_EX} {Attempt} {Fore.RESET}attempts")
                                                    input()
                                                    exit(0)
                                            elif '"status_code": 2091' in req:
                                                if NoSpam == 0:
                                                    Attempt += 1
                                                    print(
                                                        f"\r[-] Attempt : {Attempt}", end='')

                                    for x in range(Thread * 10):
                                        thread = threading.Thread(
                                            target=check).start()
                                        [].append(thread)
                                    else:
                                        for x2 in ():
                                            x2.join()

                                else:
                                    return set_bio()

                            set_bio()
                        else:
                            return set_nickname()

                    set_nickname()
                else:
                    if '"status_code": 2070' in req_check_sessionid:
                        os.system('cls')
                        print(req_banner)
                        print(f"[-] Sessionid : {sessionid}")
                        print(f"[-] Target : {username}")
                        print(f"[-] Thread : {Thread}")
                        print(
                            f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Login{Fore.RESET}")
                        print(
                            f"[{Fore.LIGHTYELLOW_EX}-{Fore.RESET}] {Fore.LIGHTYELLOW_EX}You Can Change Username After 30 day{Fore.RESET}")
                        print(
                            f"[{Fore.LIGHTRED_EX}-{Fore.RESET}] Press Enter To Exit {Fore.RESET}")
                        input()
                        exit(0)
                    else:
                        if '"status_code": 8' in req_check_sessionid:
                            os.system('cls')
                            print(req_banner)
                            print(f"[-] Sessionid : {sessionid}")
                            print(f"[-] Target : {username}")
                            print(f"[-] Thread : {Thread}")
                            print(
                                f"[{Fore.LIGHTRED_EX}-{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Failed Login {Fore.RESET}")
                            print(
                                f"[{Fore.LIGHTRED_EX}-{Fore.RESET}] Press Enter To Exit {Fore.RESET}")
                            input()
                            exit(0)
                        else:
                            return check_sessionid()

            check_sessionid()

        start()
    except FileNotFoundError:

        def start_settings():
            NameBanner = input('[-] Enter NameBanner : ')
            MessageClaim = input('[-] Enter MessageClaim With [@] : ')
            nickname = input('[-] Enter NickName : ')
            Bio = input('[-] Enter Bio : ')
            with open('SettingsTikTok.txt', 'a') as (SettingsTikTok):
                SettingsTikTok.write(
                    f"[+] NameBanner : {NameBanner}\n[+] MessageClaim : {MessageClaim}\n[+] NickName : {nickname}\n[+] Bio : {Bio}")
            os.system('cls')
            req_banner = requests.get(
                f"http://artii.herokuapp.com/make?text={NameBanner}").text
            print(req_banner)
            sessionid = input('[-] Sessionid : ')
            username = input('[-] Target : ')
            Thread = int(input('[-] Thread : '))
            Attempt = 0
            MessageBox = ctypes.windll.user32.MessageBoxW

            def check_sessionid():
                url_check_sessionid = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                headers_check_sessionid = {'Host': 'api2-t2.musical.ly',
                                           'Connection': 'close',
                                           'Content-Length': '655',
                                           'Accept-Encoding': 'gzip, deflate',
                                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                           'User-Agent': 'com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'}
                data_check_sessionid = 'unique_id=ff'
                cookies_check_sessionid = {'sessionid': sessionid}
                print('\r[-] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[\\] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[|] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[/] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[-] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[\\] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[|] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[/] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[-] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[\\] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[|] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[/] Wait To Check Sessionid', end='')
                time.sleep(0.2)
                print('\r[-] Wait To Check Sessionid', end='')
                req_check_sessionid = requests.post(
                    url_check_sessionid, headers=headers_check_sessionid, data=data_check_sessionid, cookies=cookies_check_sessionid).text
                if '"status_code": 2091' in req_check_sessionid:
                    os.system('cls')
                    print(req_banner)
                    print(
                        f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Login" + Fore.RESET)
                    time.sleep(2)

                    def set_nickname():
                        url_set_nickname = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                        headers_set_nickname = {'Host': 'api2-t2.musical.ly',
                                                'Connection': 'close',
                                                'Content-Length': '655',
                                                'Accept-Encoding': 'gzip, deflate',
                                                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                                'User-Agent': 'com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'}
                        data_set_nickname = f"nickname={nickname}"
                        cookies_set_nickname = {'sessionid': sessionid}
                        req_set_nickname = requests.post(
                            url_set_nickname, headers=headers_set_nickname, data=data_set_nickname, cookies=cookies_set_nickname).text
                        if '"status_code": 0' in req_set_nickname:
                            print(
                                f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Set Nickname {Fore.RESET}To {Fore.LIGHTYELLOW_EX}{nickname}" + Fore.RESET)
                            time.sleep(2)

                            def set_bio():
                                url_change_bio = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                                headers_change_bio = {'Host': 'api2-t2.musical.ly',
                                                      'Accept': '*/*',
                                                      'Content-Type': 'application/x-www-form-urlencoded',
                                                      'Accept-Encoding': 'gzip, deflate',
                                                      'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
                                                      'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
                                                      'Content-Length': '19',
                                                      'Connection': 'close'}
                                cookies_change_bio = {'sessionid': sessionid}
                                data_change_bio = f"signature={Bio}"
                                response_change_bio = requests.post(
                                    url_change_bio, data=data_change_bio, cookies=cookies_change_bio, headers=headers_change_bio).text
                                if '"status_code": 0' in response_change_bio:
                                    print(
                                        f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Set Bio {Fore.RESET}To {Fore.LIGHTYELLOW_EX}{Bio}" + Fore.RESET)

                                    def check():
                                        global Attempt
                                        global NoSpam
                                        url = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233'
                                        headers = {'Host': 'api2-t2.musical.ly',
                                                   'Connection': 'close',
                                                   'Content-Length': '655',
                                                   'Accept-Encoding': 'gzip, deflate',
                                                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                                   'User-Agent': 'com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'}
                                        data = f"unique_id={username}"
                                        cookies = {'sessionid': sessionid}
                                        while True:
                                            req = requests.post(
                                                url, headers=headers, data=data, cookies=cookies).text
                                            if 'unique_id' in req:
                                                if NoSpam == 0:
                                                    NoSpam = 1
                                                    os.system('cls')
                                                    print(req_banner)
                                                    print(
                                                        f"[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] All threads successfully initialized")
                                                    print(
                                                        f"[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] Swapped username {Fore.LIGHTGREEN_EX}@{username} {Fore.RESET}after{Fore.LIGHTGREEN_EX} {Attempt} {Fore.RESET}attempts")
                                                    input()
                                                    exit(0)
                                            elif '"status_code": 2091' in req:
                                                if NoSpam == 0:
                                                    Attempt += 1
                                                    print(
                                                        f"\r[-] Attempt : {Attempt}", end='')

                                    for x in range(Thread):
                                        thread = threading.Thread(
                                            target=check).start()
                                        [].append(thread)
                                    else:
                                        for x2 in ():
                                            x2.join()

                                else:
                                    return set_bio()

                            set_bio()
                        else:
                            return set_nickname()

                    set_nickname()
                else:
                    if '"status_code": 2070' in req_check_sessionid:
                        os.system('cls')
                        print(req_banner)
                        print(f"[-] Sessionid : {sessionid}")
                        print(f"[-] Target : {username}")
                        print(f"[-] Thread : {Thread}")
                        print(
                            f"[{Fore.LIGHTGREEN_EX}-{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully Login{Fore.RESET}")
                        print(
                            f"[{Fore.LIGHTYELLOW_EX}-{Fore.RESET}] {Fore.LIGHTYELLOW_EX}You Can Change Username After 30 day{Fore.RESET}")
                        print(
                            f"[{Fore.LIGHTYELLOW_EX}-{Fore.RESET}] Press Enter To Exit{Fore.RESET}")
                        input()
                        exit(0)
                    else:
                        if '"status_code": 8' in req_check_sessionid:
                            os.system('cls')
                            print(req_banner)
                            print(f"[-] Sessionid : {sessionid}")
                            print(f"[-] Target : {username}")
                            print(f"[-] Thread : {Thread}")
                            print(
                                f"[{Fore.LIGHTYELLOW_EX}-{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Failed Login {Fore.RESET}")
                            print(
                                f"[{Fore.LIGHTYELLOW_EX}-{Fore.RESET}] Press Enter To Exit {Fore.RESET}")
                            input()
                            exit(0)
                        else:
                            return check_sessionid()

            check_sessionid()

        start_settings()

else:
    print(f"[-] Your IP : {ip}")
    input()
