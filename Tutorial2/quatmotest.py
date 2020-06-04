f = open("Tutorial2/quatmo.txt", "r")
for l in f:
    print(l)
f = open("Tutorial2/quatmo.txt", "a")
while True:
    s = input("Nhap cau tho:")
    if s == "end":
        break
    f.write(s+"\n")
f.flush()
f.close()
