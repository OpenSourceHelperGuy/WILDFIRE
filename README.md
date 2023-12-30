# WILDFIRE
WILDFIRE is a lightning fast CLI designed to make basic website recon approachable for less technical users while retaining its usefulness for technical work.

**Your IP will be present in Shodan's logs unless a VPN is used.**

If you would rather use Tor than your own IP or a VPN that is something that can be done by running the tor standalone program as a system wide SOCKS5 proxy, more advice can be found in FIRE.py.

<h2>Current OPSEC Issues</h2>
There are confirmed <b>DNS leaks</b>

![image](https://github.com/OpenSourceHelperGuy/WILDFIRE/assets/151247917/ea63b23a-ba46-4d36-9696-4cc7c152928b)

These are going to be fixed with a <a href="https://quad9.net/service/service-addresses-and-features#rec"> DNS over TLS </a>/<a href="https://quad9.net/service/service-addresses-and-features#rec">DNS over HTTPS</a> Quad9 connection.

A DNS query is made to the <b>target website</b> as well as to '<b>internetdb.shodan.io</b>'.
