class conVat:
    def __init__(self):
        self.nam_sinh = "nam_sinh"
        self.ho = "ho"
        self.moi_truong = "moi_truong"

    def nhap(self):
        self.nam_sinh = input("Nhap nam sinh: ")
        self.ho = input("Nhap ho: ")
        self.moi_truong = input("Nhap moi truong: ")

    def xuat(self):
        print("Ho:" + self.ho + " , Nam Sinh: " + self.nam_sinh + ", Moi truong: " + self.moi_truong)


class thuCung(conVat):
    def __init__(self):
        conVat.__init__(self)
        self.ma = "0"
        self.ten = "0"
        self.giong = "0"

    def nhap(self):
        conVat.nhap(self)
        self.ma = input("Nhap ma: ")
        self.ten = input("Nhap ten: ")
        self.giong = input("Nhap giong: ")

    def xuat(self):
        print(self.ma + " " + self.ten + " " + self.nam_sinh + " " + self.giong + " " + self.moi_truong + " " + self.ho)

    def toStr(self):
        return str(
            self.ma + ", " + self.ten + ", " + self.nam_sinh + ", " + self.giong + ", " + self.moi_truong + ", " + self.ho + "\n")

    def constructor(self, ma, ten, nam_sinh, giong, moi_truong, ho):
        self.ma = ma
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.giong = giong
        self.moi_truong = moi_truong
        self.ho = ho


class QLDS():
    def __init__(self, dscv):
        self.dscv = dscv

    def themCV(self, cv):
        self.dscv.append(cv)

    def xoaCV(self, ma):
        for i in self.dscv:
            if i.ma == ma:
                self.dscv.remove(i)

    def countHo(self, ho):
        count = 0
        for i in self.dscv:
            if i.ho == ho:
                count = count + 1
        return count

    def show(self):
        for i in self.dscv:
            i.xuat()

    def writeToFile(self, filename):
        f = open(filename, 'w+')
        f.write("Ma, Ten, Giong, Ho, Nam Sinh, Moi Truong\n")
        for i in self.dscv:
            f.write(i.toStr())

    def readFromFile(self, filename):
        with open(filename, "r") as ins:
            for line in ins:
                dt = line.split(', ')
                print(dt)
                tc = thuCung()
                tc.constructor(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5])
                self.dscv.append(tc)


dscv = []
# tc1 = thuCung()
# tc1.nhap()
# dscv.append(tc1)
# tc2 = thuCung()
# tc2.nhap()
# dscv.append(tc2)
#
# tc3 = thuCung()
# tc3.nhap()
# dscv.append(tc3)

ql = QLDS(dscv)
ql.readFromFile('input.txt')
ql.show()
# ql.writeToFile('qltc.txt')