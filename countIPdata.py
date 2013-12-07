#!/usr/bin/python

# Kyle Jorgensen, CS284
# Script to take in the destination IP addresses from our capture data, then 
#   strip the URL's that have long CDN names, and then count the overall 
#   occurences and store them in a dictionary. Once they are organized by 
#
#   < key: top-level-domain-name, value: count-of-occurences >
#
#   then we output this data to another file.

import os
import sys
import operator
from collections import defaultdict

def readToDictionary(infile):
    '''
    Takes a text file of all the occurences of destination IP addresses. It adds these to a dictionary where each key is the URL and the value is the count of how many times it appears in the file.
    '''

    ip_dict = defaultdict(int)
    ip_data_file = open(infile,'r')

    for line in ip_data_file:

        # if it's one of the weird cases with two IP's separated with a comma 
        if ',' in line:
            for item in line.split(','):
                ip_dict[item.strip()] += 1
        else:
            #otherwise, just add it
            ip_dict[line.strip()] += 1

    ip_data_file.close()

    return ip_dict


def sortAndShortenURLs(ip_dict, precision):
    '''
    Takes a dictionary with our IP data, and returns a list of tuples of shortened URLs and the count of how many times they appear. The final result is sorted by count, in decreasing order.

    Precision is the amount that we want to shorten URLs. For example with precision 3, "csil.cs.ucsb.edu" becomes "*.cs.ucsb.edu"
    '''
    
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    
    for k, v in ip_dict.items():        
        if len(k) > 0 and k[-1] not in numbers:
            # There are some URL's that start with numbers, but a real URL cannot end 
            # in a number. So, if it is a URL with name resolution, shorten it
            url_list = k.split(".")
            
            # with precision=2, "stuff.website.com" will become "website.com" 
            new_entry = url_list[-(precision):]
            new_entry = ["*"] + new_entry

            # remove the old, long url from the dictionary
            del ip_dict[k]

            # add the new, short version
            shortened = ".".join(new_entry)
            ip_dict[shortened] += v
        elif len(k) == 0:
            print "*** k had length " + str(len(k)) + " and the value in the dictionary was " + str(v) + "\n"

    return sorted(ip_dict.items(), key=operator.itemgetter(1), reverse=True)

def writeOutput(outfilePath, tuples):
    outfile = open(outfilePath, 'w')
    
    for k, v in tuples:
        outfile.write(k + " " + str(v) + "\n")
        
    outfile.close()

#####################################################


if len(sys.argv) < 4:
    print "Usage: python countIPdata.py <inputfile> <outputfile> <precision> \n"
else:
    current = os.getcwd()
    filename = current + "/" + sys.argv[1]
    outputFile = current + "/" + sys.argv[2]
    
    data = readToDictionary(filename)
    sorted_data = sortAndShortenURLs(data,int(sys.argv[3]))
    writeOutput(outputFile, sorted_data)
    
    print "*** Finished! You can find your data in " + outputFile +'\n'

    


