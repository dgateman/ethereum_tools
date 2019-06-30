from collections import OrderedDict
from sys import argv

from decimal import Decimal
from time import sleep
from pprint import pprint as pp
SLEEP_TIME =  5
TOTAL_TIME = 500*600

CRED = '\033[91m'
CGREEN = '\033[92m'
CEND = '\033[0m'

def Print_dictionary(data):
    max_len = max([len(value) for value in data.values()])

    for i in range(max_len):
        for key, value in data.items():
            if i == 0:
                print(key + ' ' + value[i], end='        ')
            else:
                print(key + ' ' + value[i], end='  ')

        print('')


def main():
    # filename = argv[1]
    filename = 'dataset1.txt'

    for y in range(int(TOTAL_TIME/SLEEP_TIME)):
        data = Make_dictionary(filename)

        Print_dictionary(data)
        sleep(SLEEP_TIME)



def Make_dictionary(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [y.replace('\n', '') for y in data]

        data_set = OrderedDict()
        pool = []
        for i, each in enumerate(data):
            key = each.split()[0]
            value = Decimal(each.split()[1])
            if i == 0:
                pool.append(value)
                continue
            prev_key = data[i - 1].split()[0]
            if key == prev_key:
                pool.append(value)
                if i == len(data) - 1:
                    data_set[key] = pool
                continue
            else:
                data_set[prev_key] = pool
                pool = []
                pool.append(value)
                if i == len(data) - 1:
                    data_set[key] = pool
                continue

    for key, list_values in data_set.items():
        data = []
        for i, each in enumerate(list_values):
            if i == 0:
                data.append(str(each))
                continue
            prev_value = Decimal(list_values[i - 1])
            value = Decimal(each)
            diff = (value - prev_value) / prev_value * 100
            diff = round(diff, 2)
            if diff > 0:
                diff = str(value) + CGREEN + '+' + "{0:.2f}".format(diff) + '%' + CEND
            elif diff == 0:
                diff = str(value) + ' nc   '
            else:
                diff = str(value) + CRED + "{0:.2f}".format(diff) + '%' + CEND
            data.append(diff)
        data_set[key] = data
    return data_set


if __name__ == '__main__': main()

