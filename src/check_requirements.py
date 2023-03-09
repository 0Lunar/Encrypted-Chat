import sys

def check_req():
    try:
        import requests
        print(" Requirements: Ok")
    except:
        print(" Error: install first the requirements")
        sys.exit()