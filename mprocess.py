# mp.py takes any input and adds Mask Processor 64 output to the end of the word
# This is used for generating better permutations of passwords 
# E.g. if I have a password file with the 5 most common passwords, say they're "Password", "Password123", "123456", "qwerty"," abc123" and so on
# This script will add any generated list to the end of each of the passwords
# so if I type "mp.py ?n" (?n generates all 1 character numbers 0-9. ?n?n would be 0-99, etc). 
# then my output would contain this: Password0 Password1 Password2 Password3 Password4 Password5, etc. One per line
# for the second password, it would be Password1230 Password1231 Password1232, etc. One per line
# mp2.py does the same thing except places the generated characters before the password instead of after
# e.g. mp2.py passwordlist.txt ?n = 1Password 2Password 3Password 4Password
from subprocess import Popen
import sys
from pprint import pprint as pp


def main():
    if len(sys.argv) < 3:
        print("input filename and a mask as an args")
        return 0
    else:
        filename = sys.argv[1]

    with open(filename, 'r') as file:
        lines = file.readlines()

    filepath = "mp64"

    output = []
    for line in lines:
        line = line.replace('\n', '')
        if line == '':continue
        p = Popen(['mp64 ' + '"{}"'.format(line + sys.argv[2])], shell=True)
        std, stderr = p.communicate()

if __name__ == '__main__': main()

