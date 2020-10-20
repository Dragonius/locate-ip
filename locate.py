"""
    Reads table.tex and outputs a bar plot of the blocked ips' countries.

    Input: iptables list: sudo iptables -L -n --line >> table.txt
    Requests needs to be installed: sudo pip install requests

"""

import matplotlib

import datetime
import csv
import matplotlib.pyplot as plt

import requests

from collections import Counter

infile = "table.txt"

#outfile = "output.txt"
outplot = "barplot3.png"

#########
def luejaparsi():
    lista = []
    with open(infile,'r') as f:
        for line in f:
            if 'DROP' in line:
                lista.append(line.split()[4])
    return lista

def locate(iplista):
    loclist = []
    for ip in iplista:
        r = requests.get("https://ip2c.org/" + ip)
        location = r.content.split(';')[2]
        loclist.append(location)
    return loclist

def rank_list(inputlist):
    c = Counter(inputlist)
    namelist = []
    amountlist = []
    for name, amount in c.most_common():
        namelist.append(name)
        amountlist.append(amount)
    #print c
    return namelist, amountlist


def plotlist(labels, values):
    dictionary = plt.figure()
    plt.bar(range(len(values)),values, align='center')
    plt.xticks(range(len(values)), labels,rotation=90)
    #plt.ylabel("")
    plt.tight_layout()
    plt.savefig(outplot)


#locate(luejaparsi())
lab, val = rank_list(locate(luejaparsi()))

print (lab)
print (val)

#with open('country.csv', 'w' ) as file:
#    writer = csv.writer(file, delimiter=' ', quotechar=' ')
#    writer.writerows(lab)

f = open('country.csv', 'w')

with f:

    writer = csv.writer(f)
    
    for row in val:
        writer.writerow([row])
    for row in lab:
            writer.writerow([row])

# join two at a time
data_tuples = zip(lab[::2], val[1::2])
print str((data_tuples))

#with open('outputfile.txt', 'w') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerows([name + [location] for name, location in data_tuples])




#plotlist(lab, val)
