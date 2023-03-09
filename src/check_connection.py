import requests, sys

def check_connection():
    try:
        requests.get("http://google.com")
        print(" Connection: OK")
    except requests.ConnectionError:
        print(" Connection: Error.")
        sys.exit()
