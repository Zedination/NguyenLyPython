import numpy as np
import matplotlib.pyplot as plt
import string
def countOneline(x,s):
    for k in x:
        n = s.count(k)
        x[k] = x[k]+n
    return x

def removezero(y):
    s = string.ascii_lowercase
    a = list(s)
    i = len(y)-1
    while i>0:
        if y[a[i]]==0:
            del y[a[i]]
        i = i-1
    return y

def frequenceAlphabet(x,fname):
    f = open(fname,"r")
    for line in f:
        x = countOneline(x,line.lower())
    return x
s = string.ascii_lowercase
a = list(s)
n = np.zeros(len(a))

x = np.linspace(-2*np.pi,2*np.pi,200)
ysin = np.sin(x)
coords = zip
x = (("a",0),("b",0),("z",0))


x = dict(zip(a,n))
fname = input("Ten file: ")

y = frequenceAlphabet(x,fname)
y = removezero(x)
labels = list(y.values())

x = np.arange(len(labels))
