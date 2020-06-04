from mysql.connector import connect
from flask import Flask, request, jsonify

app = Flask(__name__)
connection = connect(host='localhost', database='python_db', user='root', password='')

print('Attempting to connect to the database...')
if connection.is_connected():
    print("Connection to the database established successfully")


@app.route('/', methods=['GET'])
def home():
    return "<h1> Hello </h1>"


def display_all_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products;")
    records = cursor.fetchall()

    heading = f"Total product in the system: {cursor.rowcount}"
    print(heading)
    print("-" * len(heading))
    for row in records:
        print(f"id: {row[0]}")
        print(f"name: {row[1]}")
        print(f"price: {row[2]}\n")

    cursor.close()
    connection.close()
    print("MySQL connection is closed")


def get_list():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products;")
    records = cursor.fetchall()
    return records


def add_new_product(product):
    sql_stmt = """INSERT INTO products (id,name,price) VALUES (%s,%s,%s)"""

    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt, product)
    connection.commit()
    cursor.close()
    print("Record successfully inserted into the database using prepared stament")


def update_product(product):
    sql_stmt = "UPDATE products SET name = %s,price = %s WHERE id = %s"

    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt, product)
    connection.commit()
    cursor.close()


def delete_product(id):
    sql_stmt = "DELETE FROM products WHERE id = %s"
    param = str(id)
    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt, param)
    connection.commit()
    cursor.close()


def transformData(product):
    productJson = [
        {
            "id": product[0],
            "name": product[1],
            "price": product[2]
        }
    ]
    return productJson


@app.route('/products', methods=['GET'])
def get_list_api():
    products = get_list()
    productJson = []
    for product in products:
        productJson.append(transformData(product))
    return jsonify({"message": "OK", "products": productJson})


@app.route('/addProduct', methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        id = data['id']
        name = data['name']
        price = data['price']
        product = (id, name, price)
    add_new_product(product)
    return jsonify({"message": "Add success"})


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    products = get_list()
    productJson = transformData(products[id])
    return jsonify({"message": "OK", "product": productJson})


@app.route('/products/<int:id>', methods=['PUT'])
def update(id):
    if request.method == 'PUT':
        data = request.get_json()
        name = data['name']
        price = data['price']
        product = (name, price, id)
    update_product(product)
    return jsonify({"message": "Update success"})


@app.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        delete_product(id)
    return jsonify({"message": "Xoá thành công!"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)