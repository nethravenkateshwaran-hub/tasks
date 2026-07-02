import mysql.connector as nethra

def nethra_connect():
    """Helper function to quickly open our communication connection channel."""
    return nethra.connect(
        host="localhost",
        user="root",
        password="Nn@cmd123",
        database="sql1",
        auth_plugin='mysql_native_password'
    )

def create_record():
    print("\n--- NETHRA: INSERT NEW RECORD ---")
    roll = input('enter roll: ')
    name = input('enter name: ')
    phone = input('enter phone no: ')
    course = input('enter course: ')
    
    mydb = nethra_connect()
    mycursor = mydb.cursor() # mediator
    
    # Inserting using standard %s placeholder layout
    mycursor.execute(
        "INSERT INTO register(roll, name, phone, course) VALUES (%s, %s, %s, %s)",
        (roll, name, phone, course)
    )
    mydb.commit()
    print("Value inserted successfully!")
    
    mycursor.close()
    mydb.close()

def read_records():
    print("\n--- NETHRA: DISPLAYING ALL RECORDS ---")
    mydb = nethra_connect()
    mycursor = mydb.cursor() # mediator
    
    mycursor.execute("SELECT * FROM register")
    my = mycursor.fetchall()
    
    if not my:
        print("No records found inside the register table.")
    else:
        for i in my:
            print(i)
            
    mycursor.close()
    mydb.close()

def update_record():
    print("\n--- NETHRA: UPDATE EXISTING RECORD ---")
    roll = input('enter roll to target: ')
    name = input('enter new name: ')
    phone = input('enter new phone no: ')
    course = input('enter new course: ')
    
    mydb = nethra_connect()
    mycursor = mydb.cursor() # mediator
    
    # Updating fields matching the exact roll identifier
    mycursor.execute(
        "UPDATE register SET name = %s, phone = %s, course = %s WHERE roll = %s",
        (name, phone, course, roll)
    )
    mydb.commit()
    print("Value updated successfully!")
    
    mycursor.close()
    mydb.close()

def delete_record():
    print("\n--- NETHRA: DELETE A RECORD ---")
    roll = input('enter roll to delete: ')
    
    mydb = nethra_connect()
    mycursor = mydb.cursor() # mediator
    
    # Target and wipe a single entry using its unique roll string/number
    mycursor.execute("DELETE FROM register WHERE roll = %s", (roll,))
    mydb.commit()
    print("Value deleted successfully!")
    
    mycursor.close()
    mydb.close()

def main():
    """Looping interaction control interface."""
    while True:
        print("\n==============================")
        print("    NETHRA'S CRUD TERMINAL APP ")
        print("==============================")
        print("1. Insert Record (Create)")
        print("2. View All Records (Read)")
        print("3. Modify Record (Update)")
        print("4. Remove Record (Delete)")
        print("5. Exit Application")
        
        choice = input("\nSelect an operational choice (1-5): ")
        
        if choice == '1':
            create_record()
        elif choice == '2':
            read_records()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            print("\nShutting down application interface. Goodbye Nethra!")
            break
        else:
            print("\nInvalid menu option context. Please input figures 1 through 5.")

if __name__ == "__main__":
    main()
