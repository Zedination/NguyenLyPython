# with open("test.txt",'a+',encoding = 'utf-8') as f:
#     data = input("Nhap vao: ")
#     f.write(data)
#     print("Them thanh cong")
#
def themDuLieuVaoFile(fileName, data):
    f = open(fileName, 'a+', encoding='utf-8')
    f.write(data + '\n')


filename = input("Nhap ten File: ")
while True:
    data = input("Nhap data: ")
    if data == 'end':
        break
    themDuLieuVaoFile(filename, data)
