import requests
import sys

def find(domain):
    return [line.split(',')[0] for line in requests.get(f'https://api.hackertarget.com/hostsearch/?q={domain}').text.splitlines()]

print(find(sys.argv[1]))