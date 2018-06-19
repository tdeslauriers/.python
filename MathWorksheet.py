#imported libraries
import random

#text variable initialization
firstline0 = ""
secondline0 = ""
space0 = []
for d in range(0, 10):
    space0.append(" ")

#array variable initialization
line0 = []
line1 = []
sign0 = []
rVals = []

r0 = 10
r1 = 100
r2 = 1000
rVals.append(r0)
rVals.append(r1)
rVals.append(r2)

#generates random numbers
def num0(r):
    t = random.randrange(1, r)
    return t

#makes random choice between "+" and "-"
def sign():
    a = random.randrange(0,2)
    if a == 0:
        b = "+"
    else:
        b = "-"
    return b

#loop thru loading arrays
def arrays0(i, j, k, l):
    for x in range(0, 8):
        i.append(num0(l))
        j.append(num0(l))
        if i[x] < j[x]:
            k.append("+")
        else:
            k.append(sign())

#function to produce text lines from arrays
def output0(q, r, t):
    n = 0;
    for d in t:
        if len(str(d)) == 1:
            q = q + "%s  %d          " %(r[n], d)
        elif len(str(d)) == 2:
            q = q + "%s %d          " %(r[n], d)
        else:
            q = q + "%s%d          " %(r[n], d)
        n = n + 1
    return q

#writes output to .txt file
def display1(a, b, c, d, e, f):
    mathPrac = open("mathPrac.txt", "w")
    v = 0
    for z in range(0,3):
        arrays0(a, b, d, rVals[v])
        mathPrac.write("Level %d (%d points):\n\r" %(v+1, v*2+2))
        o = str(output0(e, c, a))
        mathPrac.write(o + "\r")
        p = str(output0(e, d, b))
        mathPrac.write(p + "\r")
        n = ("----          ")
        mathPrac.write("%s%s%s%s%s%s%s%s\r" %(n, n, n, n, n, n, n, n))
        mathPrac.write("\n\r\n\r\n\r\n\r")
        a = []
        b = []
        d = []
        v = v + 1
    mathPrac.close()

display1(line0, line1, space0, sign0, firstline0, secondline0)
