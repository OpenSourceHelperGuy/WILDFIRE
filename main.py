import os
import sys
import socket
import pprint
import time
import dns.message
import dns.query
# from dns.doh import DoHSession # Fix at 3
import requests
# import random # could be used to add random splash messages under the banner
from pystyle import Colors, Colorate, Write

# https://github.com/spyboy-productions/CloakQuest3r - Helps with Cloudflare bypasses
if sys.platform == "win32":
    try:
        import win32gui
        import win32con
    except:
        pass
# TODO - ensure that DNS leakage is fixed urgently with DoH running on 443 as DoT runs on a unique port and can be blocked
# resolver = dns.resolver.Resolver()
# resolver.nameservers = ["9.9.9.9"]  # not confirmed working - 9.9.9.9 has DNSSEC however may cause problems when researching malware sites
# TODO - the backup resolver 9.9.9.10 should be used if 9.9.9.9 times out or responds with a "domain blocked" type message

try:
    os.system("title WILDFIRE")
except:
    pass

if sys.platform == "win32":
    # Maximise the screen
    try:
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    except:
        pass


def banner_print():
    banner = '''
                                                                                             
    *@@@@*     @     *@@@**@@@@**@@@@*    *@@@***@@m  *@@@***@@@*@@@@**@@@***@@m  *@@@***@@@ 
      *@@     m@@     m@    @@    @@        @@    *@@m  @@    *@  @@    @@   *@@m   @@    *@ 
       @@m   m@@@m   m@     @@    @@        @@     *@@  @@   @    @@    @@   m@@    @@   @   
        @@m  @* @@m  @*     @@    @@        @@      @@  @@**@@    @@    !@@@@@@     @@@@@@   
        !@@ @*  *@@ @*      @!    @!     m  @!     m@@  !@   @    @!    !@  @@m     @@   @  m
         !@@m    !@@m       @!    @!    :@  @!    m@!*  !@        @!    !@   *!@    @!     m@
         !!@!*   !!@!*      !!    !!     !  !!     !!!  !!        !!    !@  ! !!    !!   !  !
         !!!!    !!!!       :!    !:    !!  !:    !!:*  :!        :!    !!   *!!!   !!     !!
          :       :       :!: : : :: !: : : : : : :   :!: :     :!: : : :!:  : : :: :::!: : :
                                                                                             
            '''
    Write.Print(banner, Colors.red_to_yellow, interval=0.01)
    print(Colorate.Horizontal(Colors.red_to_yellow,
                              'Now uses Shodan!                                                 Is your VPN on?', 1))


if __name__ == '__main__':
    banner_print()


def recon():
    while True:
        web_target = input('\n\nWhich website do you want the IP(s) for? [e.g example.com] ')
        try:
            web_target = str(web_target)
        except:
            print("Invalid input")
            time.sleep(3)
            sys.exit()

        def get_ips_for_host(host):
            global web_target_ip
            web_target_ip = 1
            socket.setdefaulttimeout(5)  # Set socket time out to 5 seconds
            try:
                # Attempt at Quad9 DoH using the dnspython module #TODO - Urgent

                ''' Error 400 ground up attempt at Quad9 DoH using Requests
                # web_target_ip = socket.  gethostbyname_ex(host) # does DNS query that leaks web_target's name // DNS leaks to host?
                # TODO - prevent DNS leakage // look above for potential Quad9 DoH solution

                quad9_doh = 'https://dns.quad9.net/dns-query'  # Quad9 DoH that doesn't leak web_target's name
                # DNS query parameters
                headers = {
                    'Method': 'GET',
                    'Scheme': 'https',
                    'Content-Type': 'application/dns-json',
                    'Accept': 'application/dns-json'

                }

                params = {
                    'name': web_target,
                    'type': 'A'
                }

                # Send a GET request to Quad9 DoH endpoint
                web_target_ip = requests.get(quad9_doh, params=params, verify=True, allow_redirects=True, headers=headers, timeout=5   )
                # Process the response
                if web_target_ip.status_code == 200:
                    # Parse the response content
                    web_target_ip = web_target_ip.json()

                else:
                    print(f'\nQuad9 DoH has responded with the code {web_target_ip.status_code}.')

            except requests.RequestException as e:
                print(e)
                # Handle request connection/response errors
                '''
            except socket.gaierror:
                print('\nNo IP was found.\nIs the website online?\nIs your internet connection working?')
                web_target_ip = []

            finally:
                # Reset the default timeout to its previous value (optional)
                socket.setdefaulttimeout(None)

            return web_target_ip

        ips = get_ips_for_host(web_target)

        print('\n')  # \n doesn't work with pprint.pprint
        pprint.pprint(repr(ips))

        # FIRE
        import FIRE
        FIRE.scan()


recon()
