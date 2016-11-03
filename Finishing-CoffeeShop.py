#David Justice
#11-2-16
#Completing the Coffee Shop

import sqlite3


def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("\nThe table [0] already exists, do you wish to recreate it (y/n): " .format(table_name))
            if response == "y":
                 keep_table = False
                 print("\nthe {0} table will be recreated - all existing data will be lost\n" .format(table_name))
                 cursor.execute("drop table if exists {0}".format(table_name))
                 db.commit()
            else:
                 print("\nthe existing table was kept\n")
        else:
            keep_table = False
            cursor.execute(sql)
            db.commit()


def create_product_table():
    sql = """create table Product
             (ProductID integer,
             Name text,
             Price real,
             ProductTypeID integer,
             primary key(ProductID),
             foreign key(ProductTypeID) references ProductType(ProductTypeID))"""
    create_table(db_name, "Product", sql)

def create_product_type_table():
    sql = """create table ProductType
             (ProductTypeID integer,
             Description text,
             primary key(ProductTypeID))"""
    create_table(db_name, "ProductType", sql)

def create_customer_table():
    sql = """create table Customer
             (CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode integer,
             TelephoneNumber integer,
             EMailAddress text,
             primary key(CustomerID))"""
    create_table(db_name, "Customer", sql)

def create_customer_order_table():
    sql = """create table CustomerOrder 
             (OrderID integer,
             Date text,
             Time text,
             CustomerID integer,
             primary key(OrderID)
             foreign key(CustomerID) references Customer(CustomerID))"""
    create_table(db_name, "CustomerOrder", sql)   

def create_order_item():
    sql = """create table OrderItem
             (OrderItemID integer,
             OrderID integer,
             ProductID integer,
             Quantity integer,
             primary key(OrderItemID)
             foreign key(OrderID) references CustomerOrder(OrderID)
             foreign key(ProductID) references Product(ProductID))"""
    create_table(db_name, "OrderItem", sql)

    
if __name__ == "__main__":
    db_name = "coffee_shop.db"
    create_product_table()
    create_product_type_table()
    create_customer_table()
    create_customer_order_table()
    create_order_item()
