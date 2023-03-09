import socket, sys, getpass
from src import enc_dec

def send_command(s):
    while True:
        try:
            command = " " + getpass.getuser() + " => " + input(" => ")
            command = command
            if(command == "ESC"):
                print(" Closing connection...")
                s.close()
                sys.exit()
            else:
                s.send(command.encode())
                data = s.recv(4096)
                data = enc_dec.decrypt_file(str(data, "utf-8"))
                if data != (command):
                    print("\n" + data + "\n")
        except KeyboardInterrupt:
            print("\n Closing connection...")
            s.close()
            sys.exit()