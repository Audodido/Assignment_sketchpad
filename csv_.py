# import csv
# import sys

# with open(sys.argv[1], 'rt') as f:
#     reader = csv.reader(f)
#     val = 0

#     for row in reader:
#         if val < 5: #this is so we just see first 5 lines -- lose the if to see all lines
#             print(row)
#             val += 1

## https://stackoverflow.com/questions/53172771/how-to-take-csv-file-as-an-input
## same thing as above but using argparse

import sys
import argparse
import csv
from os import read

parser = argparse.ArgumentParser('csv', description="Taking in csv filepath")
parser.add_argument('csv', help="enter the filename--make sure the file's in the program directory")
args = parser.parse_args()

with open(args.csv, 'rt') as csvFile:
    val = 0
    reader = csv.reader(csvFile)
    for row in reader:
        if val < 5: #this is so we just see first 5 lines -- lose the if to see all lines
            print(row)
            val += 1

