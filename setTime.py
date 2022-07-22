import sys
import os
import re
from datetime import datetime
import time
import pyprctl

def _linux_set_time():
    print(sys.argv)
    try:
        date = sys.argv[1]
    except IndexError:
        pass
    try:
        tps = sys.argv[2]
    except IndexError:
        pass
    if date:
        trame = date
        timestamp = time.mktime(datetime.strptime(trame, "%Y-%m-%d").timetuple())
    elif tps:
        trame = tps
        timestamp = time.mktime(datetime.strptime(trame, "%H:%M:%S").timetuple())
    elif tps and date:
        trame = date + ' ' + tps
        timestamp = time.mktime(datetime.strptime(trame, "%Y-%m-%d %H:%M:%S").timetuple())
    else :
        print("BAD FORMAT")
        exit(1)
    print(timestamp)
    time.clock_settime(time.CLOCK_REALTIME, timestamp)

if __name__ == '__main__':
    #Drop all caps if they are not sysTime
    for cap in pyprctl.caps.Cap:
        if str(cap) == 'Cap.SYS_TIME' :
            pyprctl.capbset_drop(cap)
    _linux_set_time()
