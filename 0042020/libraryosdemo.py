import os
from os import path
import glob

print(os.getcwd())
link = input("Nhap vao duong dan: ")
if path.exists(link):
    print("Dung lượng của thư mục: ", os.stat(link).st_size)
else:
    print("Đường dẫn sai!")