import os
import sys
import socket
import pprint
# import random # could be used to add random splash messages under the banner
# import dns.resolver # import requires "pip install dnspython"
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
                              "Now uses Shodan!                                                 Is your VPN on?", 1))


if __name__ == '__main__':
    banner_print()


def recon():
    while True:
        web_target = input('\n \nWhich website do you want the IP for? [e.g example.com] ')

        # scan_port = input('\nWhich port would you like to scan? ')
        def get_ips_for_host(host):
            socket.setdefaulttimeout(5) # Set socket time out to 5 seconds
            try:

                web_target_ip = socket.gethostbyname_ex(host) # does DNS query that leaks web_target's name
                # TODO - prevent DNS leakage // look above for potential Quad9 DoH solution

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
