# Reader file created to read a .csv file from excel and assign contents
# to an object

# Actual data transfer to db would happen elsewhere.

import argparse # access to optional commandline arguments
# Haven't added this yet!

import os.path  # access to isfile

print "Hello world!"

print """
This is a CSV file uploader. It will upload your files and automagically
store the data into a database."""

# todo: alternatively we want to read this as an argument to the file

#if arg_file == "":
arg_file = raw_input("Enter filename: ")    # get the name of the .csv file

try:

    os.path.isfile(arg_file)
    
    infile = open(arg_file, 'r')    # open the .csv file for reading
        # not exactly sure, is an error catching thing, ensures file is
        # closed even if an exception occurs

    for line in infile:     # for each line in the infile list
        print line,         # print line contents

    infile.close()  # Close the csv input file

except IOError as e:
   print 'Oh dear. File cannot be opened.'
