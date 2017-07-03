import sys
def get_ip(ip):
    a = 0
    b = 0
    c = 0
    d = 0
    temp = ip
    a = temp&0xff
    temp = temp >> 8
    b = temp&0xff
    temp = temp >> 8
    c = temp&0xff
    temp = temp >> 8
    d = temp&0xff
    print "IP = ",a,".",b,".",c,".",d


get_ip(52428)
