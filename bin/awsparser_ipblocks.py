#!/usr/bin/env python3
"""
This is a sample of the script to build regex
"""

import sys
import json
import netaddr

IPLIST = list()
INPUTFILE = str(sys.argv[1])

with open(INPUTFILE) as fileobj:
    with open(INPUTFILE, 'r') as jsonfile:
        AWSIPDICT = json.load(jsonfile)

for block in AWSIPDICT['prefixes']:
    if block['ip_prefix']:
        NSTRING = (str(block['ip_prefix']))
        (nbase, nprefix) = NSTRING.split('/')
        IPLIST.append(netaddr.IPNetwork(NSTRING))
        ### print(NSTRING)

### print('### Original: {}'.format(len(set(IPLIST))))
SUMMARY = netaddr.cidr_merge(IPLIST)
### print('### Consolidated: {}'.format(len(set(SUMMARY))))
for ipblock in SUMMARY:
    print(str(ipblock))
