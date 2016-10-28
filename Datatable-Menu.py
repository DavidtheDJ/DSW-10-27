#David Justice
#10-27-16
#Task 9 - Pulling it Together
#Menu Program

import sqlite3

##################################################################################################################

def menu():

    print("\nProduct Table Menu\n")
    print("1. (Re)Create Product Table")
    print("2.  Add new product")
    print("3.  Edit existing product")
    print("4.  Delete existing product")
    print("5.  See product list")
    print("6.  Search for products")
    print("0.  Exit")
    print("")

    def responseAnswer():
        
        response = input("Please select an option number: ")
        
        if response == "1":
            creatingDatatable()
        elif response == "2":
            addingData()
        elif response == "3":
            changingData()
        elif response == "4":
            deletingData()
        elif response == "5":
            returnData()
        elif response == "6":
            searchData()
        elif response == "0":
            print("\nGoodbye!")
        else:
            print("\nPlease enter a vaild opition number.\n")
            responseAnswer()
    
    responseAnswer()
    
##################################################################################################################  

def creatingDatatable():

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
            if not keep_table:
                cursor.execute(sql)
                db.commit()
            menu()

    if __name__ == "__main__":
        db_name = "coffee_shop.db"
        sql = """create table Product
                 (ProductID integer,
                 Name text,
                 Price real,
                 primary key(ProductID))"""
        create_table(db_name, "Product", sql)

    menu()

##################################################################################################################

def addingData():
    
    def insert_data(values):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "insert into Product (Name, Price) values (?,?)"
            cursor.execute(sql,values)
            db.commit()

    def insertCycle():
        
        insertRequestName = input("\nWhat would you like to add?")
        insertRequestPrice = float(input("What should it's price be?"))

        if __name__ == "__main__":                          
            product = (insertRequestName, insertRequestPrice)
            insert_data(product)

        def insertRestart():
            insertContinue = input("\nWould you like to add another product?(y/n)")
                                           
            if insertContinue == "y":              
                insertCycle()
            elif insertContinue == "n":
                menu()
            else:
                print("\nPlease type 'y' for yes or 'n' for no\n")
                insertRestart()
                
        insertRestart()
        
    insertCycle()

##################################################################################################################

def changingData():

    def update_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "update Product set Name=?, Price=? where ProductID=?"
            cursor.execute(sql,data)
            db.commit()

    def updateCycle():
        
        updateRequestName = input("\nWhat would you like to update?")
        updateRequestPrice = float(input("What should it's price be?"))

        if __name__ == "__main__":
            data = (updateRequestName, updateRequestPrice,1)
            update_product(data)

        def updateRestart():
            
            updateContinue = input("\nWould you like to update another product?(y/n)")
                                           
            if updateContinue == "y":              
                updateCycle()
            elif updateContinue == "n":
                menu()
            else:
                print("\nPlease type 'y' for yes or 'n' for no\n")
                updateRestart()

        updateRestart()

    updateCycle()

##################################################################################################################

def deletingData():
    def delete_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "delete from Product where Name=?"
            cursor.execute(sql,data)
            db.commit()

    def deleteCycle():
        
        deleteRequestName = input("\nWhat would you like to delete?")

        if __name__ == "__main__":
            data = (deleteRequestName,)
            delete_product(data)

        def deleteRestart():
            
            deleteContinue = input("\nWould you like to delete another product?(y/n)")
                                           
            if deleteContinue == "y":              
                deleteCycle()
            elif deleteContinue == "n":
                menu()
            else:
                print("\nPlease type 'y' for yes or 'n' for no\n")
                deleteRestart()

        deleteRestart()

    deleteCycle()

    menu()

##################################################################################################################

def returnData():

    def select_all_products():
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Product")
            products = cursor.fetchall()
            return products

    if __name__ == "__main__":
        products = select_all_products()
        print(products)

    menu()

##################################################################################################################

def searchData():
    
    def select_product(id):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute("select Name,Price from Product where ProductID=?",(id,))
            product = cursor.fetchone()
            return product
        
    def searchCycle():
        
        searchRequestName = input("\nWhat would you like to search for?(Type item postition)\n")

        if __name__ == "__main__":
            product = select_product(searchRequestName)
            print(product)

        def searchRestart():
            
            searchContinue = input("\nWould you like to search for another product?(y/n)")
                                           
            if searchContinue == "y":              
                searchCycle()
            elif searchContinue == "n":
                menu()
            else:
                print("\nPlease type 'y' for yes or 'n' for no\n")
                searchRestart()

        searchRestart()

    searchCycle()

##################################################################################################################

menu()




























