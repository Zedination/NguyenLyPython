# Bài 1.1: Tạo 1 chương trình yêu cầu người dùng nhập tên và tuổi của họ. In ra 1 thông báo cho họ nói với họ
# rằng năm mà họ sẽ tròn 100 tuổi


name = input("Tên bạn là gì: ")
age = input("Bạn bao nhiêu tuổi: ")
so = input("Số lần thông báo: ")
nam = 2020+100-int(age)
print("năm bạn 100 tuổi là năm: ", nam)
print("Bạn [0] sống đến năm [1] sẽ có tuổi là 100", format(name,str(nam)))




