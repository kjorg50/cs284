# cs284 Scripts


## Count IP Data
This script takes in the destination IP addresses from our capture data, strips the URL's that have long CDN names, and then counts the number of overall occurences of each URL/IP address. We hope this allows us to see the most commonly accessed websites in our packet captures.

The script is run with the following format:

```
python countIPdata.py <inputfile> <outputfile> <precision>
```

So, if this were a sample input file

```
128.111.87.112
a771.da1.akamai.net
gauchospace.ucsb.edu,17.151.230.4
ec2-23-23-226-62.compute-1.amazonaws.com
128.111.87.112
128.111.87.112
gauchospace.ucsb.edu
```

And if I used precision equal to 2, the following output would be created:

```
128.111.87.112 3
*.ucsb.edu 2
*.akamai.net 1
*.amazonaws.com 1
17.151.230.4 1
```

