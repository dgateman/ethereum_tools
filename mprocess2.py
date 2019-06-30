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
        #pp(lines)

    filepath = "/usr/bin/mp64"

    output = []
    for line in lines:
        #std = None
        line = line.replace('\n', '')
        if line == '':continue
        p = Popen(['/usr/bin/mp64 ' + '"{}"'.format(sys.argv[2] + line)], shell=True)
        std, stderr = p.communicate()
        
        #print(type(std))        
#print(stdout)
        #output.append(std.copy())
    #print(output)
    #output = '\n'.join(output)
    #with open(filename.split('.')[0] + '_output.txt', 'w') as file:
     #   file.write(output)
if __name__ == '__main__': main()

