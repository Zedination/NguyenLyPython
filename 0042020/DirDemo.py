import os
import time
def compSizeofPath(path):
    if os.path.exists(path):
        count=0
        numf = 0
        for x in  os.walk(path):
            for f in x[2]:
                count = count + os.stat(x[0]+"\\" + f).st_size
                numf = numf  + 1
        if count <1024:
            print("{} bytes".format(count))
        else:
            if count<1024*1024:
                print("{:.3f} Kbs".format(count/(1024)))
            else:
                if count <1024*1024*1024:
                    print("{:.3f} Mbs".format(count/(1024*1024)))
                else:
                    print("{:.3f} Gbs".format(count/(1024*1024*1024)))
        print("Tổng số file: {}".format(numf))
    else:
        print("{} không tồn tại, hãy kiểm tra lại.".format(path))

path = input("Nhap duong dan den thu muc:")
s = time.time()
compSizeofPath(path)
e = time.time()
print("Thời gian tính toán: {}".format((e-s)))