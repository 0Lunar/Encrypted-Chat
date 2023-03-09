import sys
from src.check_requirements import check_req
from src.server.sub_server import sub_server
from src.server.get_text import get_text
from src.client.clean import clean
from src.check_connection import check_connection

if __name__ == "__main__":
    clean()
    check_req()
    check_connection()
    host_name = input("\n Enter the host address => ")
    port = int(input("\n Enter the port => "))
    host = (str(host_name), port)
    clean()
    conn = sub_server(host)
    get_text(conn)