import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host = 'localhost',database = 'qlbh',user = 'root',password = '')
    if conn.is_connected():
        print("Kết nối đến database thành công")
        insert_query = 'insert into tbluser value("aaaa","aaa","aaa","aaa","aaa","aaa")'
        cusr = conn.cursor()
        cusr.execute(insert_query)
        conn.commit()
        print("Số bản ghi được thực hiện: ",cusr.rowcount)
        cusr.close()
except Error as e:
    print("Kết nối thất bại, lỗi: ", e)