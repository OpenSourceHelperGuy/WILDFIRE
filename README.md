# WILDFIRE
WILDFIRE is a lightning fast CLI designed to make basic website recon approachable for less technical users while retaining its usefulness for technical work. (Now with 100% more Shodan 😳)

**Your IP will be present in Shodan's logs unless a VPN is used.**

If you would rather use Tor than your own IP or a VPN that is something that can be done by running the tor standalone program as a system-wide SOCKS5 proxy, more advice can be found in FIRE.py.

<h2>Current OPSEC Issues</h2>
There are confirmed <b>DNS leaks</b>

![image](https://github.com/OpenSourceHelperGuy/WILDFIRE/assets/151247917/ea63b23a-ba46-4d36-9696-4cc7c152928b)

These are going to be fixed with a <a href="https://quad9.net/service/service-addresses-and-features#rec">DNS over HTTPS</a> Quad9 connection.

A DNS query is made to the <b>target website</b> and to '<b>internetdb.shodan.io</b>'.



There are <b>SNI leaks</b>
TLS 1.3 is used however the Server Name Indication in the Client Hello is leaked in plaintext. ![image](https://github.com/OpenSourceHelperGuy/WILDFIRE/assets/151247917/cf92824a-5bf8-432b-a138-7497ab5ac275)
This can be fixed by implementing <a href="https://en.wikipedia.org/wiki/Server_Name_Indication#Encrypted_Client_Hello">Encrypted Client Hello (ECH)</a> however this also depends on the web server to support ECH and so is not as simple of a fix as DoH. And there is no formal implementation of ECH in Python so currently the only solution is to use (a) VPN/Tor.
