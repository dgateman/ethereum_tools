import random
import sys


def main():
    if len(sys.argv) < 3:
        print("Please specify the arguments")
        sys.exit()
    repeat = sys.argv[1]
    filename = sys.argv[2]

    with open(filename, 'w') as file:
        for i in range(int(repeat)):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            c = random.randint(0, 10)
            d = random.randint(0, 10)
            e = random.randint(0, 10)
            file.write("""perl -lane 'print "$F[{}] $F[{}] $F[{}] $F[{}] $F[{}]"' filename >> file\n""".format(a, b, c, d, e))


if __name__ == '__main__': main()
