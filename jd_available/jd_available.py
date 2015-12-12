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

Кроме того скрипт использует библиотеку PyQt4. В Ubuntu:
    sudo apt-get install python3-pyqt4

Вызов скрипта:
    python3 jd_available.py <id товара>
'''

import os
import sys
import http.client
import pyglet
import time

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4.phonon import Phonon

def achtung():
    BASE_DIR = os.path.dirname(__file__)
    a = pyglet.resource.media(os.path.join(BASE_DIR, 'achtung.wav'))
    a.play()
    pyglet.clock.schedule_once(lambda x: pyglet.app.exit(), a.duration)
    pyglet.app.run()


class App(QApplication):
    def __init__(self, argv, url):
        QApplication.__init__(self, argv)
        self.url = url
        self.n = 0
        self._request_page()

    def _request_page(self):
        self.page = QWebPage(self)
        self.page.loadFinished.connect(self._check_goods)
        self.page.mainFrame().load(QUrl(self.url))

    def _check_goods(self, result):
        self.n += 1
        print('Попытка:', self.n)
        if result:
            content = self.page.mainFrame().toHtml()
            unavailable = '<span class="c-red off-sale-tip" style="display: inline;">unavailable</span>'
            available = '<span class="c-red off-sale-tip">unavailable</span>'
            if unavailable in content:
                print('Товар НЕ доступен.')
            elif available in content:
                print('УРА. Товар доступен.')
                print('Ссылка на товар:', site + page)
                achtung()
            else:
                print('Нет информации о доступности товара.')
                achtung()
        else:
            print('Нет ответа от JD.com.')
            achtung()

        QTimer.singleShot(5000, self._request_page)


if len(sys.argv) < 2:
    print(help_text);
    exit()

product_id=sys.argv[1]

site='en.jd.com'
page = '/product/' + product_id + '.html'

print('Ссылка на товар:', site + page)

app = App(sys.argv, 'http://' + site + page)
app.exec_()
