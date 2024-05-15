from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(f"[+] {tgtPort} tcp Open")

    except:
        print(f"[+] {tgtPort} tcp Closed")
    finally: 
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"Unknown Host {tgtHost}")

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"[+] Scan Results for: {tgtName[0]}")
    except:
        print(f"[+] Scan Results for: {tgtIP}")

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    Host = input("Enter the host to scan: ")
    Ports = input("Enter the ports to scan: ").split(',')
    portScan(Host, Ports)

if __name__ == "__main__":
    main()
