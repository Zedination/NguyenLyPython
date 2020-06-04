import matplotlib.pyplot as plt
import numpy as np
import string


def countOneLine(x, line):
    for k in x:
        n = line.count(k)
        x[k] = x[k] + n
    return x


def removeZero(y):
    s = string.ascii_lowercase
    a = list(s)
    i = len(y) - 1
    while i > 0:
        if y[a[i]] == 0:
            del y[a[i]]
        i = i - 1
    return y


def frequenceAlphabet(x, fname):
    f = open(fname, 'r')
    for line in f:
        x = countOneLine(x, line)
    return x


s = string.ascii_lowercase
a = list(s)
n = np.zeros(len(a))
x = dict(zip(a, n))
fname = 'news.txt'
x = frequenceAlphabet(x, fname)
x = removeZero(x)
labels = list(x.keys())
val = list(x.values())
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x, val, width, label='Freq')
ax.set_ylabel('Frequence')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
