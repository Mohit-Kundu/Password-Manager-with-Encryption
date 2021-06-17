import sqlite3
import sys

#change to 'login.db'
conn = sqlite3.connect('login.db')

cur = conn.cursor()

#Only run first time to create table
'''cur.execute("""CREATE TABLE login (
                website text,
                username text,
                password text
    )""")'''

#Adding new login details
def add_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
        password = input('Enter password: ')

        #log = LOGIN('website', 'username', 'password')

        cur.execute("INSERT INTO login VALUES(?, ?, ?)", (website, username, password))
        print("Password added successfully")

#Retrieving login details
def get_password():
    website = input('Enter website: ')
    username = input('Enter username: ')

    try:
        cur.execute("SELECT password FROM login WHERE website = ? AND username = ?", (website, username))
        print("Password: {}".format(cur.fetchone()))

    except :
        print("Username / Website doesn't exist in records")

#Updating password
def update_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
        password =  input('Enter updated password: ')

        try:
            cur.execute("UPDATE login SET password = ? WHERE website = ? and username = ?",  (password, website, username))
            print('Password updated successfully')
        
        except:
            print("Username / Website doesn't exist in records")

#Deleting password
def delete_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
    
        try:
            cur.execute("DELETE from login WHERE website = ? and username = ?", (website, username))
            print("Password deleted successfully")
        
        except Exception as e:
            print("Username / Website doesn't exist in records")

if __name__ == '__main__':
    print("""Press: \n
    1. To ADD a Password\n
    2. To GET a Password\n
    3. To UPDATE a Password\n
    4. To DELETE a Password\n
    or any other key to EXIT...\n
    """)

    choice =  input("Enter your choice: ")

    if choice == '1':
        add_password()

    if choice == '2':
        get_password()

    if choice == '3':
        update_password()
    
    if choice == '4':
        delete_password()
    
    else:
        conn.close()
        sys.exit()