#!/usr/bin/env python
'''convert the nuclear strand to antisense strand'''
def aq_antisense_strand(line):
    list_anti=[]
    for i in line:
        if i =='A':
            list_anti.append('T')
        elif i=='T':
            list_anti.append('A')
        elif i =='G':
            list_anti.append('C')
        elif i =='C':
            list_anti.append('G')
        elif i =='N':
            list_anti.append('N')
    return ''.join(list_anti)
if __name__=='__main__':
    import sys
    for line in open(sys.argv[1]):
    	aq_antisense_strand(line)
