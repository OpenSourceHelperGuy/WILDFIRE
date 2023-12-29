import os
import sys
import socket
import pprint
# import random # could be used to add random splash messages under the banner
# import dns.resolver # import requires "pip install dnspython"
# from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Write  # Add, Box,
# https://github.com/spyboy-productions/CloakQuest3r - Helps with Cloudflare bypasses
try:
    import win32gui
    import win32con
except:
    pass

# resolver = dns.resolver.Resolver()
# resolver.nameservers = ["9.9.9.10"]  # not confirmed working - should be unfiltered Quad9 DNS resolution

if sys.platform == "win32":
    os.system("title WILDFIRE")
# Maximise the screen
    try:
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    except:
        pass


def banner_print():
    banner = """
                                                                                         
*@@@@*     @     *@@@**@@@@**@@@@*    *@@@***@@m  *@@@***@@@*@@@@**@@@***@@m  *@@@***@@@ 
  *@@     m@@     m@    @@    @@        @@    *@@m  @@    *@  @@    @@   *@@m   @@    *@ 
   @@m   m@@@m   m@     @@    @@        @@     *@@  @@   @    @@    @@   m@@    @@   @   
    @@m  @* @@m  @*     @@    @@        @@      @@  @@**@@    @@    !@@@@@@     @@@@@@   
    !@@ @*  *@@ @*      @!    @!     m  @!     m@@  !@   @    @!    !@  @@m     @@   @  m
     !@@m    !@@m       @!    @!    :@  @!    m@!*  !@        @!    !@   *!@    @!     m@
     !!@!*   !!@!*      !!    !!     !  !!     !!!  !!        !!    !@  ! !!    !!   !  !
     !!!!    !!!!       :!    !:    !!  !:    !!:*  :!        :!    !!   *!!!   !!     !!
      :       :       :!: : : :: !: : : : : : :   :!: :     :!: : : :!:  : : :: :::!: : :
                                                                                         
        """
    Write.Print(banner, Colors.red_to_yellow, interval=0.01)
    print(Colorate.Horizontal(Colors.red_to_yellow,
                              "Now uses Shodan!                                                 Is your VPN on?", 1))


if __name__ == '__main__':
    banner_print()


def recon():
    while True:
        web_target = input("\n \nWhich website do you want the IP for? [e.g example.com] ")

        # scan_port = input("\nWhich port would you like to scan? ")
        def get_ips_for_host(host):
            try:
                web_target_ip = socket.gethostbyname_ex(host)
            except socket.gaierror:
                print("\nNo IP was found.\nIs the website online?\nIs your internet connection working?")
                web_target_ip = []
            return web_target_ip

        ips = get_ips_for_host(f"{web_target}")
        print("\n")  # \n doesn't work with pprint.pprint
        pprint.pprint(repr(ips))
        # FIRE
        import FIRE
        FIRE.scan()


recon()
