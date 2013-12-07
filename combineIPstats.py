#!/usr/bin/python

# Script to take two of the output files from countIPdata.py and combine the 
#  sets of data.

import os
import sys
import operator
from collections import defaultdict

def combineSets(file1, file2, result):
    ''' 
    Take the IP data from two files and combine it into one
    '''

    result_dict = defaultdict(int)
    
    # Read the data from the first file into the dictionary
    fileOne = open(file1,'r')
    for line in fileOne:
        temp_line = line.split()
        result_dict[temp_line[0]] += int(temp_line[1])
    fileOne.close()

    # Read the data from the second file into the dictionary
    fileTwo = open(file2,'r')
    for aLine in fileTwo:
        temp_line = aLine.split()
        if len(temp_line) == 2:
            result_dict[temp_line[0]] += int(temp_line[1])
        else:
            print "*** failed on second file, content = " + str(temp_line) + '\n'
    fileTwo.close()
    
    # sort the combined data
    sortedData = sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True)

    # write it to the output file
    outfile = open(result, 'w')
    for k, v in sortedData:
        outfile.write(k + " " + str(v) + "\n")
    outfile.close()



####################################################
if len(sys.argv) < 4:
    print "Usage: python combineIPstats.py <inputfile1> <inputfile2> <outputfile> \n"
else:
    current = os.getcwd()
    file1name = current + "/" + sys.argv[1]
    file2name = current + "/" + sys.argv[2]
    outfile = current + "/" + sys.argv[3]
    
    combineSets(file1name, file2name, outfile)
    
    print "*** Finished! You can find your data in " + outfile +'\n'
    
