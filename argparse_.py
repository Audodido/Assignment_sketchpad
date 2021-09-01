# https://www.youtube.com/watch?v=cdblJqEUDNo
# https://docs.python.org/3/howto/argparse.html
# argparse is the recommended command-line parsing module in the Python standard library.

import argparse

parser = argparse.ArgumentParser(description="Multiply two arguments (ints)")
# adding '--' before the arguments makes them optional arguments for the user @ terminal 
# you can add more flags to the beginning i.e. ("--burger", "-x", "-gg"...etc)
# required argument determines whether the argument is optional or needed to run program
parser.add_argument("-x", type=int, required=True, help="any ol number")
parser.add_argument("-y", type=int, required=True, help="another ol number")
args = parser.parse_args()

# simply function to multiply two ints as args
def multi(x, y):
    return x * y 


if __name__ == '__main__':
    print(multi(args.x, args.y))
    print(args.x)
    print(args.y)