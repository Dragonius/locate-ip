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
plotlist(lab, val)
