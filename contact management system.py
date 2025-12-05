import sqlite3
conn=sqlite3.connect("contact.db")
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone text(10))""")
conn.commit()


def add_contact(id,name,phone):
    cur.execute("insert INTO contact VALUES (?,?,?)",(id,name,phone))
    print("Your values are inserted successfully")
    conn.commit()
    
def view_contact():
    cur.execute("select * from contact")
    rows=cur.fetchall()
    for row in rows:
        print("ID:",row[0]," | Name:",row[1]," | Phone No.:",row[2])

def search_contact(name):
    cur.execute("select * from contact where name=?",(name,))
    rows=cur.fetchall()
    for row in rows:
        print("ID:",row[0]," | Name:",row[1]," | Phone No.:",row[2],"\n")

def update_contact(name,new_phone):
    cur.execute("update contact set phone=? where name=?",(new_phone,name))
    print("Updated successfully")
    conn.commit()

def delete_contact(name):
    cur.execute("delete from contact where name=?",(name,))
    print("Deleted Successfully")
    conn.commit()

while True:
    print("\n 1.New Contact \n 2.View Contact \n 3.Search Contact \n 4.Update Contact \n 5.Delete Contact \n 6.Exit ")
    choice=int(input("Choose an option:"))
    if choice==1:
        id=int(input("enter id:"))
        name=input("enter name:")
        phone=input("enter phone no.:")
        add_contact(id,name,phone)
    elif choice==2:
        view_contact()
    elif choice==3:
        name=input("Enter a name to search:")
        search_contact(name)
    elif choice==4:
        name=input("Enter a name to update:")
        new_phone=input("Enter new no.:")
        update_contact(name,new_phone)
    elif choice==5:
        name=input("Enter a name to delete:")
        delete_contact(name)
    elif choice==6:
        print("Exiting........")
        break
    else:
        print("Invalid Option!\nEnter another option")