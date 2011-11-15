# Reader file created to read a .csv file from excel and assign contents
# to an object
#
# Mitch LeBlanc 2011-11-14

# Haven't added this yet!
import argparse # access to optional commandline arguments

import sys  # access to sys.argv

import os.path  # access to isfile

print """
This is a CSV file uploader. It will upload your files and automagically
store the data into a database.\n"""

# todo: alternatively we want to read this as an argument to the file

if len(sys.argv) == 1:
    arg_file = raw_input("Enter filename: ")    # get the name of the .csv file
else:
    arg_file = sys.argv[1]

if not os.path.isfile(arg_file):
    sys.exit("Not a valid file name!")

if os.path.splitext(arg_file)[1] != ".csv":
    sys.exit("Not a valid file type!")

try:
    infile = open(arg_file, 'r')    # open the .csv file for reading
    print("Reading file: %s\n") % arg_file
        # not exactly sure, is an error catching thing, ensures file is
        # closed even if an exception occurs
except IOError as e:
   print 'Oh dear. File cannot be opened.'

for line in infile:     # for each line in the infile list
    print line,         # print line contents

infile.close()  # Close the csv input file


