import os
from cryptography.fernet import Fernet

value = Fernet.generate_key()
print(value)

#Saving key in .env file
with open(".env", "ab") as f:
    f.write(value)