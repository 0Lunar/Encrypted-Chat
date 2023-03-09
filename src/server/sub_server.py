import socket, sys

def sub_server(host):
    try:
        s = socket.socket()
        s.bind(host)
        s.listen()
        print(" Initialized server listening")
    except socket.error as error:
        print(f"\n Something went wrong\n Error: {error}")
        print(f"\n server is reinitializing")
        sub_server(host)
    conn, client_address = s.accept()
    print(f"\n Server - Client connection established: {host}")
    return conn
