import sqlite3

#change to 'login.db'
conn = sqlite3.connect(':memory:')

cur = conn.cursor()

''''cur.execute("""CREATE TABLE login (
                website text,
                username text,
                password text
    )""")'''

#Inserting login details
def add_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
        password = input('Enter password: ')

        log = LOGIN('website', 'username', 'password')

        cur.execute("INSERT INTO login VALUES(?, ?, ?)", (website, username, password))

#Retrieving login details
def get_password():
    website = input('Enter website: ')
    username = input('Enter username: ')

    try:
        cur.execute("SELECT * FROM login WHERE website = ? AND username = ?", (website, username))
        print(curr.fetchone())

    except Exception as e:
        print("Username / Website doesn't exist in records")

def update_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
        password =  input('Enter updated password: ')

        try:
            curr.execute("UPDATE login SET password = ? WHERE website = ? and username = ?",  (password, website, username))
        
        except Exception as e:
            print("Username / Website doesn't exist in records")

def delete_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
    
        try:
            curr.execute("DELETE FROM login WHERE website = ? and username = ?", (website, username))
        
        except Exception as e:
            print("Username / Website doesn't exist in records")
        
conn.close()