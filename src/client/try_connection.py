import sys, socket

def try_connect(host):
    try:
        s = socket.socket()
        s.connect(host)
        print(f"\n connection to {host} established\n")
        return s
    except socket.error as error:
        print(f"\n Something went wrong\n Error: {error}")
        sys.exit()