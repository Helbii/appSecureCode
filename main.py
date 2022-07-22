# This is a sample Python script.
from myLib import getDate,setDate, hashfile, read_port
import threading
from http.server import BaseHTTPRequestHandler
from flask import Flask, render_template, request
import logging
import pyprctl
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.parse_request()

hostName = "localhost"

serverPort = read_port(_file='/etc/port.txt')

myClock = {
    'getDate': getDate,
    'setDate': setDate
}
#http://127.0.0.1:5000/ webpage
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

    #pyprctl.capbset_drop(pyprctl.caps.cap_permitted)#clear all the capabilities
    print(hashfile())
    #pyprctl.capbset_drop(pyprctl.get_keepcaps())
    for cap in pyprctl.caps.Cap:
        pyprctl.capbset_drop(cap)
        #print(cap.name)
    #print("caps"+str(pyprctl.Cap))
    command = commandsList[0]
    while True:
        print('commands : ' + commandsList[0] + ',' + commandsList[1] + '\n')
        command = input('Send ur command\n')

        if command == 'getDate':
            print('choose ur format : %D/%M/%Y %H:%M:%Y\n')
            format = input('Send ur fomat\n')
            message=myClock[command](_format=format)
            print(message)

        elif command == 'setDate':
            print('format : YYYY-MM-DD HH:MM:SS or YYYY-MM-DD or HH:MM:SS')
            newDate = input('Set ur new date\n')
            myClock[command](_newDate=newDate, _hash=hash)

        else:
            print('command does not exist')


if __name__ == '__main__':

    threading.Thread(target=local_request, args=(myClock, commandsList)).start()
    threading.Thread(target=lambda: app.run(port=serverPort)).start()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
