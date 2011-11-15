# Reader file created to read a .csv file from excel and assign contents
# to an object
#
# Mitch LeBlanc 2011-11-14

# import argparse # access to optional commandline arguments, currently unused

import sys  # access to sys.argv, and exit

import os.path  # access to isfile

# A little intro message
print """
This is a CSV file uploader. It will upload your files and automagically
store the data into a database.\n"""

# todo: alternatively we want to read this as an argument to the file

if len(sys.argv) == 1:  # There needs to be TWO arguments if filename is there
    arg_file = raw_input("Enter filename: ")    # get the name of .csv file
else:
    arg_file = sys.argv[1]  # The second argument (index 1) is the file name

# Just a quick check to see if file name is a valid file
if not os.path.isfile(arg_file):
    sys.exit("Not a valid file name!")

# Check to see if the file is called .csv (though we don't really care)
if os.path.splitext(arg_file)[1] != ".csv":
    sys.exit("Not a valid file type!")

# Try to open the file, catch the exception if it fails?
try:
    infile = open(arg_file, 'r')    # open the .csv file for reading
    print("Reading file: %s\n") % arg_file  # Echo the file name

except IOError as e:    # if file open failed for whatever reason
   print 'Oh dear. File cannot be opened.'

for line in infile:     # for each line in the infile list
    print line,         # print line contents

infile.close()  # Close the csv input file


