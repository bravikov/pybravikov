help_text='''
Скрипт каждые 5 секунд проверяет доступность товара на jd.com и в случае
доступности делает звуковое уведомление (файл achtung.wav).

Скрипт принимает в качестве аргумента id товара, который содержится в
ссылке на товар. Например, в этой ссылке (en.jd.com/product/860975.html)
id равен 860975.

Если скрипт не может связаться с сайтом, то он выдает то же звуковое
уведомление и продолжает попытки.

Скрипт использует библиотеку pyglet для воспроизведения звука. Команда
для установки библиотеки в Linux:
    sudo pip3 install pyglet

Вызов скрипта:
    python3 jd_available.py <id товара>
'''

import sys
import http.client
import pyglet
import time

if len(sys.argv) < 2:
    print(help_text);
    exit()

product_id=sys.argv[1]

site='en.jd.com'
page = '/product/' + product_id + '.html'

print('Ссылка на товар:', site + page)

connection = http.client.HTTPConnection(site)

def achtung():
    a = pyglet.resource.media('achtung.wav')
    a.play()
    pyglet.clock.schedule_once(lambda x: pyglet.app.exit(), a.duration)
    pyglet.app.run()

n = 0
while True:
    n += 1
    print('Попытка:', n)

    connection.request('GET', page)

    try:
        response = connection.getresponse()
    except http.client.HTTPException:
        print('Что-то пошло не так.')
        achtung()
        continue

    if response.status != 200:
        print(response.status, response.reason)
        achtung()
        continue

    content = response.read().decode('utf-8')

    if 'unavailable' not in content:
        print('Ура. Товар доступен.')
        achtung()

    time.sleep(5)
