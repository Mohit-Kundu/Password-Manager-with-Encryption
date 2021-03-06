import sqlite3
from cryptography.fernet import Fernet
import sys
import os
import pyperclip

#Add pyperclip support

conn = sqlite3.connect('login.db')

cur = conn.cursor()

#Only run first time to create table
'''cur.execute("""CREATE TABLE login (
                website text,
                username text,
                password text
    )""")'''

crypt = Fernet(os.getenv('KEY'))

#Adding new login details
def add_password(website, username, password):
    with conn:
        encrypted_pw = crypt.encrypt(password) # Encryption

        cur.execute("INSERT INTO login VALUES(?, ?, ?)", (website, username, encrypted_pw))
        print("New password added successfully")

#Retrieving login details
def get_password(website, username):
    cur.execute("SELECT password FROM login WHERE website = ? AND username = ?", (website, username))

    try:
        password = crypt.decrypt(cur.fetchone()[0])  # cur.fetchone returns a tuple, to get a string we need to index it
        print("Password: {}".format(password.decode("utf-8")))

        pyperclip.copy(password.decode("utf-8"))
        print("Password copied to clipboard")
    
    except: # NoneType is not supscriptable
        print("Website / Username doesn't exist in records")

#Updating password
def update_password(website, username, password):
    with conn:
        encrypted_pw = crypt.encrypt(password) # Encryption

        #Fetching records where website and username match
        cur.execute("SELECT password FROM login WHERE website = ? AND username = ?", (website, username))

        if(len(cur.fetchall()) == 0): #No matches
            print("Website / Username doesn't exist in records")
            add_password(website, username, password)

        else:
            cur.execute("UPDATE login SET password = ? WHERE website = ? and username = ?",  (encrypted_pw, website, username))
            print('Password updated successfully')

#Deleting password
def delete_password(website, username):
    with conn:
        #Fetching records where website and username match
        cur.execute("SELECT password FROM login WHERE website = ? AND username = ?", (website, username))

        if(len(cur.fetchall()) == 0): #No matches
            print("Website / Username doesn't exist in records")
        
        else:
            cur.execute("DELETE from login WHERE website = ? and username = ?", (website, username))
            print("Password deleted successfully")

if __name__ == '__main__':

    print("""Press: \n
    1. To ADD a Password\n
    2. To GET a Password\n
    3. To UPDATE a Password\n
    4. To DELETE a Password\n
    or any other key to EXIT...\n
    """)

    choice =  int(input("Enter your choice: "))

    if(choice not in range(1,5)): #Exiting
        conn.close()
        sys.exit()

    website = input('Enter website: ')
    username = input('Enter username / email id: ')

    if choice == 1:
        password = input('Enter password: ').encode('utf-8') # Converting password to bytes for encryption
        add_password(website, username, password)

    if choice == 2:
        get_password(website, username)

    if choice == 3:
        password =  input('Enter updated password: ').encode('utf-8')
        update_password(website, username, password)
    
    if choice == 4:
        delete_password(website, username)