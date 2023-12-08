import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="behnam"
)
mycursor = mydb.cursor()

sql = "CREATE DATABASE shop_management9"

mycursor.execute(sql)



def create_products_table():
    sql = """
        CREATE TABLE products(
        product_id INT AUTO_INCREMENT,
        product_name VARCHAR(255),
        category_id INT,
       price INT,quantity INT,
        PRIMARY KEY ( product_id),FOREIGN KEY (category_id) REFERENCES categories_table (category_id)
        );
    """
    cursor.execute(sql)
    connection.commit()

def create_categories_table():
    
    sql = """
        CREATE TABLE categories(
        category_id INT AUTO_INCREMENT,
        category_name VARCHAR(255),
        PRIMARY KEY ( category_id)
        );
    """
    cursor.execute(sql)
    connection.commit()

def add_product(product_id, product_name, category_id, price, quantity):
    cursor.execute(f'INSERT INTO products (product_id, product_name, category_id, price, quantity) VALUES ({product_id},{product_name},{category_id, price},{ price},{ quantity})')
    connection.commit()

def add_category(category_id, category_name):
    cursor.execute(f'INSERT INTO categories (category_id, category_name) VALUES ({category_id}, "{category_name}")')
    connection.commit()

    
def remove_product(product_id):
    cursor.execute('DELETE FROM products WHERE product_id = {product_id}')
    connection.commit()
    
def remove_category(category_id):
    cursor.execute(f'DELETE FROM categories WHERE category_id = {category_id}')
    connection.commit()


def edit_product(product_id, product_name, category_id, price, quantity):
    cursor.execute(f'UPDATE products SET product_name = {product_name}, category_id = {category_id}, price = {price}, quantity = {quantity} WHERE product_id = {product_id}')
    connection.commit()

def edit_category(category_id, category_name):
    cursor.execute(f'UPDATE categories SET category_name = {category_name} WHERE category_id = {category_id}')
    connection.commit()


def search_product_by_name(product_name):
    cursor.execute(f'SELECT * FROM products WHERE product_name LIKE { product_name}')
    product = cursor.fetchall()
    return product


def search_product_by_category(category_name):
    cursor.execute(f'SELECT * FROM categories WHERE product_name LIKE { category_name}')
    product = cursor.fetchall()
    return product

def show_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)


def show_all_categories():
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    for category in categories:
        print(category)















