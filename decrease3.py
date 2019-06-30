import sys
from time import sleep
from subprocess import Popen

SLEEP_TIME = 5


def main():

    filename = 'theprice.txt'

    if len(sys.argv) <= 1:
        sys.exit('please specify the number as an argument')

    NUMBER = float(sys.argv[1])

    while True:
        try:
            f = open(filename, 'r')
            file_value = f.read()
            value = float(file_value.replace(' ', '').replace('\n', ''))
            print(value)
        except Exception as e:
            print(e)
            print(file_value)
            sleep(SLEEP_TIME)
            continue
        else:
            file_value = value
        if file_value <= NUMBER:
            print('goal number reached {}'.format(file_value))
            p = Popen(['/home/d/.etherdata/send_email_low.bash'], shell=True)
            stdout, stderr = p.communicate()
            print(stdout)
            sys.exit(0)
        sleep(SLEEP_TIME)


if __name__ == '__main__': main()

