import socket, sys, os
from src.check_requirements import check_req
from src.check_connection import check_connection
from src.client.try_connection import try_connect
from src.client.send import send_command
from src.client.clean import clean

if __name__ == "__main__":
    clean()
    check_req()
    check_connection()
    host_address = input("\n Enter the host address => ")
    port = int(input("\n Enter the port: "))
    host = (str(host_address), port)
    establish_connection = try_connect(host)
    send_command(establish_connection)