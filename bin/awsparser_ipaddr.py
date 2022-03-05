#!/usr/bin/python3
"""
This is a sample of the script to build regex
"""

import sys
import json
import ipaddress

INPUTFILE = str(sys.argv[1])
IPLIST = list()

with open(INPUTFILE) as fileobj:
    with open(INPUTFILE, 'r') as jsonfile:
        AWSIPDICT = json.load(jsonfile)

for block in AWSIPDICT['prefixes']:
    if block['ip_prefix']:
        NSTRING = (str(block['ip_prefix']))
        (nbase, nprefix) = NSTRING.split('/')
        for ip in ipaddress.IPv4Network(NSTRING):
            IPLIST.append(ip)

### print('### Original: {}'.format(len(set(IPLIST))))

for ipaddr in IPLIST:
    print(str(ipaddr))
