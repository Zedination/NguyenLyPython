# Bài 1.2 Yêu cầu người dùng cho một số,  tùy thuộc vào số đó là số chẵn hay số lẻ, hãy in ra một thông điệp phù hợp cho người dùng. 
# Mở rộng: Nếu số đó là bội số của 4, hãy in ra một tin nhắn khác.
so = input('Nhập số ngẫu nhiên: ')
if (int(so) % 2 == 0) :
    if (int(so) % 4 ==0):
        print('Số vừa nhập là bội của 4')
    else:
        print("Số vừa nhập là số chẵn")
else:
    print("Số vừa nhập là số lẻ")