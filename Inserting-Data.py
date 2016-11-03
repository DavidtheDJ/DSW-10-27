#David Justice
#11-2-16
#Adding to Relationship Tables

import sqlite3

def query(sql,data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def insert_product_type_data(records):
    sql = "insert into ProductType(Description) values (?)"
    for record in records:
        query(sql,record)

def insert_product_data(records):
    sql = "insert into Product (Name,Price,ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql,record)

if __name__ == "__main__":
    product_types = [("Coffee",),("Tea",),("Cold Drink",)]
    insert_product_type_data(product_types)
    products = [("Americano",1.50,2),("Mocha",2.40,1),("Green Tea",1.20,2)]
    insert_product_data(products)
    products = [("Raspberry",3.50,3),("Black Tea",1.00,2),("Latte",1.35,1)]
    insert_product_data(products)
    products = [("Lemonade",2.85,3)]
    insert_product_data(products)
