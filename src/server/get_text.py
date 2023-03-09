import socket, sys
from src import enc_dec

def get_text(conn):
    while True:
        try:
            req = conn.recv(4096)
            if(req.decode() != ""):
                text = req.decode()
                print(text)
                text = enc_dec.encrypt_file(text)
                conn.send(text.encode())
        except KeyboardInterrupt:
            sys.exit()