# CS 021 final Project
# Haoyuan Pang

import requests
import json

def main():
    ip = requests.get("http://worldtimeapi.org/api/ip")
    ip = ip.json()


    print(ip["datetime"])

main()