import sys
import os
import re


def _linux_set_time():
    command = 'sudo timedatectl set-time '
    #print(sys.argv)
    trame = sys.argv[1]
    print(trame)

    dateRegex = re.search("[0-2][0-9][0-9][0-9][-][0-1][0-9][-][0-31]", trame)
    timeRegex = re.search("[0-5][0-9][:][0-5][0-9][:][0-5][0-9]", trame)
    datetimeRegex = re.search("[0-2][0-9][0-9][0-9][-][0-1][0-9][-][0-31][ ][0-5][0-9][:][0-5][0-9][:][0-5][0-9]", trame)
    print('timeregex:'+str(timeRegex))
    print('dateregex:'+str(dateRegex))

    if dateRegex or timeRegex:
        os.system(command + str(trame))
        pass
    elif datetimeRegex:
        trame = trame.split(' ')
        os.system(command + str(trame[0]))
        os.system(command + str(trame[1]))
        pass
    else:
        print('Wrong format')
        exit(1)


if __name__ == '__main__':
    _linux_set_time()
