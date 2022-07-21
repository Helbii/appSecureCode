# This is a sample Python script.
from myLib import getDate,setDate, hashfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, render_template, redirect, url_for, request
import logging

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.parse_request()

hostName = "localhost"

serverPort = 5000

hash = 'e82b0f05530c49da40abe3c0b251ee126c60f738'

myClock = {
    'getDate': getDate,
    'setDate': setDate
}

#disable flask log
log = logging.getLogger('werkzeug')
log.disabled = True

commandsList = []
for element in myClock:
    commandsList.append(element)




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def server_request():
    error = None
    message = None
    format = ''
    if request.method == 'POST':
        format = request.form['format']
        message = myClock['getDate'](_format=format)
    return render_template('home.html', error=error, message=message)


def local_request(myClock, commandsList) :
    print(hashfile())
    command = commandsList[0]
    while True:
        print('commands : ' + commandsList[0] + ',' + commandsList[1] + '\n')
        command = input('Send ur command\n')

        if command == 'getDate':
            print('choose ur format : %D/%M/%Y %H:%M:%Y\n')
            format = input('Send ur fomat\n')
            message=myClock[command](_format=format)
            print(message)

        if command == 'setDate':
            print('format : YYYY-MM-DD HH:MM:SS or YYYY-MM-DD or HH:MM:SS')
            newDate = input('Set ur new date\n')
            myClock[command](_newDate=newDate, _hash=hash)

        else:
            print('command does not exist')


if __name__ == '__main__':
    threading.Thread(target=local_request, args=(myClock, commandsList)).start()
    threading.Thread(target=lambda: app.run()).start()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
