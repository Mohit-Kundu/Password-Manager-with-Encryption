# Python-Password-Manager-with-Encryption
This is an extensive **Password Manager** built in **Python**, that can ecrypts passwords and maintains a record of the **encrypted** passwords in a **sqlite** database.

It performs the following operations:

- **Adding** new passwords
- **Fetching** pre-existing passwords from database and **copying them to clipboard**
- **Updating** pre-existing passwords
- **Deleting** pre-existing passwords

## Requirements
- Python version > = 3.0
- cryptography
- sqlite3
- pyperclip

## Getting started (Initial Setup)
1. Run key_gen.py to generate key for encryption
2. The generated key is then stored in the .env file

## Note: 
- Run key_gen.py to generate key for the first time. 
- Do not run key_gen.py again, as it will overwrite the pre-existing key used for encryption passwords
- If the key is overwritten, the manager won't be able to decrypt saved passwords

## How to run password manager?
1. Run main.py
2. Select the desired operation from list of operations by entering the corresponding number
3. To exit, enter any key ( other than the ones specified in menu )

---

