#Database connection
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",password="visshva@2005",database="library_system")
cursor=mycon.cursor()

#User authentication
def authenticate(username,password):
    query="select * from users where username=%s and password=%s"
    cursor.execute(query,(username,password))
    return cursor.fetchone()

#Adding a book
def add_book(title,author):
    query="insert into books (title,author) values (%s,%s)"
    cursor.execute(query,(title,author))
    mycon.commit()
    print("Book added successfully!")

#Viewing a book
def view_books():
    query="select * from books"
    cursor.execute(query)
    return cursor.fetchall()
    if books:
        print("Available Books:")
        for book in books:
            print(f"Book_ID: {book[0]},Title: {book[1]},Author: {book[2]},Available: {book[3]}")
    else:
        print("No books found!")

#Borrowing a book
def borrow_book(user_id,book_id):
    query="update books set available=false where book_id=%s"
    cursor.execute(query,(book_id,))
    mycon.commit()

    query="insert into activity (user_id,book_id,borrow_date) values (%s, %s, curdate())"
    cursor.execute(query,(user_id,book_id))
    mycon.commit()
    print("Book borrowed successfully!")

#Returning a book
def return_book(user_id,book_id):
    query="update books set available=true where book_id=%s"
    cursor.execute(query,(book_id,))
    mycon.commit()

    query="delete from activity where user_id=%s and book_id=%s"
    cursor.execute(query,(user_id, book_id))
    mycon.commit()
    print("Book returned successfully!")

#Main program
def main():
    print("!!! Welcome to Library Management System !!!")
    
    # User authentication
    username=input("Enter username: ")
    password=input("Enter password: ")
    user=authenticate(username, password)
    
    if user:
        print(f"Welcome {username}!")
        while True:
            print("\nChoose among these 5 options:")
            print("1. Add Book")
            print("2. View Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")
            choice=input("Enter your choice: ")
            
            if choice=="1":
                title=input("Enter book title: ")
                author=input("Enter book author: ")
                add_book(title,author)
            
            elif choice=="2":
                view_books()
            
            elif choice=="3":
                book_id=int(input("Enter book_ID to borrow: "))
                borrow_book(user[0],book_id)
            
            elif choice=="4":
                book_id=int(input("Enter book_ID to return: "))
                return_book(user[0],book_id)
            
            elif choice=="5":
                print("Thank you for logging in.")
                break
            else:
                print("Invalid choice, please try again!")
    else:
        print("Authentication failed. Please check your username and password.")

    # Closing the connection
    cursor.close()
    mycon.close()

# Run the program
if __name__ == "__main__":
    main()
