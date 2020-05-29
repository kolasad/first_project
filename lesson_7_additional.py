import sys
import os


print(dir(sys))
print(dir(os))


import builtins
print(dir(builtins))


import requests
print(requests.get('https://google.com').text)
