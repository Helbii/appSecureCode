from datetime import datetime
import hashlib
import os


def hashfile():
    """"This function returns the SHA-1 hash
      of the file passed into it"""
    # make a hash object
    h = hashlib.sha1()
    # open file for reading in binary mode
    with open('setTime.py', 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def setDate(**kwargs):
    print('hashfile = ' + hashfile())
    print(kwargs['_hash'])
    # if hashfile() == kwargs['_hash'] :
    # print('ok')
    command = 'sudo python3 setTime.py ' + str(kwargs['_newDate'])
    err = os.system(command)
    #print(err)


def getDate(**kwargs):
    dt = datetime.now()
    if kwargs['_format'] == '':
        return 'Date : ' + str(dt.today())
    else:
        try:
            return dt.strftime(kwargs['_format'])
        except NameError:
            print(NameError)


def getHours(*args, **kwargs):
    dt = datetime.now()
    return str(dt.hour)


def getDays(*args, **kwargs):
    dt = datetime.now()
    return str(dt.day)


def getMonth(*args, **kwargs):
    dt = datetime.now()
    return str(dt.month)


def getYear(*args, **kwargs):
    dt = datetime.now()
    return str(dt.year)


def getTime(*args, **kwargs):
    dt = datetime.now()
    return str(dt.time())
