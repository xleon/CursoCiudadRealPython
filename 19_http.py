"""
Ejemplo de llamada http para cargar contenido remoto
"""

from urllib import request

def load_url(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as response:
        return response.read()

ex = load_url('https://swapi.co/api/people')
# print(ex)

import requests 

response = requests.get('https://httpbin.org/ip')
print(response.json())
ip = response.json()['origin']
print('Mi ip es', ip)

response = requests.get('https://swapi.co/api/people')
people = response.json()['results']

print('\nPersonajes de Start Wars:')

for p in people:
    print(p['name'])





    