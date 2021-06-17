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

    cur.execute("SELECT * FROM login WHERE website = ? AND username = ?", (website, username))

    print(curr.fetchone())

def update_password():
    with conn:
        website = input('Enter website: ')
        username = input('Enter username: ')
        password =  input('Enter updated password: ')

        curr.execute("UPDATE login SET password = ? WHERE website = ? and username = ?",  (password, website, username))


conn.close()