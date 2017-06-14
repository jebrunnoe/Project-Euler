from decimal import *
import re
getcontext().prec = 5000
maxd = 0
maxwidth = 0

def finder(seq):
    slen = len(seq)
    for i in range(1, slen):
	if slen % i == 0:
	    if seq == (slen / i) * seq[:i]: return i
 
for d in range(2, 1000):
    match = re.match(r"^(?P<rep>.*)(?P=rep)", str(Decimal(1)/Decimal(d))[2:])
    width = finder(match.group('rep'))
    if width > maxwidth:
	maxwidth = width
	maxd = d

print maxd
