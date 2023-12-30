import sys
import os
import pprint
import requests
import time
from colorama import Fore

try:
    import win32gui
    import win32con
except ImportError:
    pass


###############################################

def banner_print():
    banner = r'''
    ___________________________________
    \_   _____/   |______   \_   _____/
      |  ___) |   ||       _/|    __)_ 
      |  \__  |   ||    |   \|        \
     /___  /  |___||____|_  /_______  /
         \/               \/        \/ 
Shodan hates Tor, I wonder what Google Translate has to say to that...
HINT: https://internetdb-shodan-io.translate.goog/{target}
        '''
    print(Fore.GREEN + banner)


infinite = 0

if __name__ == '__main__':
    infinite = 1
    try:
        os.system('title FIRE')
    except:
        pass
    # Maximise the screen
    if sys.platform == "win32":
        try:
            hwnd = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        except:
            pass
    banner_print()


def scan():
    # global run_shodan_call_once #TODO - logic for the second run asking the user to quit the program does not work
    run_shodan_call_once = 0
    while True:
        if infinite == 1:
            # If the user has run the Shodan call once before ask them if they want to close the program
            if run_shodan_call_once == 1:
                target = input("\nWhich IP do you want to analyse? ['none' to quit] ")
                if target.lower() == 'none':
                    sys.exit()
                print('\n')

            if run_shodan_call_once == 0:
                target = input('\nWhich IP do you want to analyse? [Run WILDFIRE first] [e.g 93.184.216.34] ')
                print('\n')

        if infinite == 0:
            # If the user has run the Shodan call once before ask them if they want to close the program but if FIRE.py is called from main.py
            if run_shodan_call_once == 1:
                target = input("\nWhich IP do you want to analyse? ['none' to quit] ")
                if target.lower() == 'none':
                    sys.exit()
                print('\n')

            if run_shodan_call_once == 0:
                target = input('\nWhich IP do you want to analyse? [e.g 93.184.216.34] ')
                print("\n")

        def shodan_call():

            try:
                scanned = requests.get(f"https://internetdb.shodan.io/{target}", verify=True, allow_redirects=False, timeout=5).json()
                # verify=True // verifies certificate from trusted CA // using OCSP?? if so then should be disabled as information leakage
                pprint.pprint(scanned)
                run_shodan_call_once = 1

            except requests.exceptions.SSLError:
                print('TLS certificate verification has failed.\nThis could be due to a MiTM attack.')
                time.sleep(4)
                print('\nAborting the program now...\n')
                time.sleep(2)

                if sys.platform == "win32":
                    try:
                        os.system('powershell pause')
                    except:
                        pass
                sys.exit()

            except requests.exceptions.RequestException:
                print('Failed to reach https://internetdb.shodan.io \nCheck your internet connection.\nThe website could be inaccessible.\n')
                # if infinite == 0:

                if sys.platform == "win32":
                    try:
                        os.system('powershell pause')
                    except:
                        pass
            finally:
                pass # ???
                # from FIRE import scan # ???

        shodan_call()


scan()
