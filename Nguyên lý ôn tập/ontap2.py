import os
from os import path
import glob

pat = os.getcwd()
print(pat)

# os.makedirs("ABC")  # tạo thư mục
# new_name = input("Nhap vao ten moi:")
# os.rename("ABC", new_name)  # đổi tên
open('ab1/test.txt', 'w+')  # thêm file
req = input("Ban co muốn xoá không (1/0):")
if req == '1':
    print('hello')
    os.remove('ab1/test.txt')  # xoá