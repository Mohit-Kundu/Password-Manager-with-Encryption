# Python-Password-Manager-with-Encryption
This is a **Password Manager** built using **Python** and **sqlite**, that encrypts passwords and maintains a record of the **encrypted** passwords in a database.

It performs the following operations:

- **Encrypts** passwords and **stores** them in a database
- **Fetches** pre-existing passwords from the database and **copies them to clipboard** after **decryption**
- **Updates** pre-existing passwords
- **Deletes** pre-existing passwords

## Requirements
- Python version > = 3.0
- cryptography
- sqlite3
- pyperclip

## Getting started (Initial Setup)
1. Run key_gen.py to generate key for encryption
2. The generated key is then stored in the .env file

## Note: 
- Run key_gen.py to generate key for the **first time**. 
- **Do not run key_gen.py again**, as it will overwrite the pre-existing key used for encryption passwords
- If the key is overwritten, the manager won't be able to decrypt saved passwords anymore

## How to run password manager?
1. Run main.py
2. Select the desired operation from list of operations by entering the corresponding number
3. To exit, enter any key ( other than the ones specified in menu )

---

