import os
from cryptography.fernet import Fernet

protected_files = ["encrypt.py","decrypt.py","encryption_key.key","venv"]
target_files=["sample_image.jpg"]

# Determing the files to encrypt.


# Creating the Encryption/Decryption Key (Password to be used when decrypting an encrypted content) and a Fernet Class Instance.
encryption_key = Fernet.generate_key() 
fernet_instance = Fernet(encryption_key)
with open("encryption_key.key","wb") as encryption_key_object:
	encryption_key_object.write(encryption_key)


# Encryption Process
count=0
for file in target_files:
	count += 1
	print(f"\nReading File #{count}: {file}")
	with open(file,"rb") as file_object:
		content_to_encrypt = file_object.read()
	encrypted_content = fernet_instance.encrypt(content_to_encrypt)
	with open(file,"wb") as file_object:
		file_object.write(encrypted_content)
	print(f"Encrypted '{file}'")

print(f"\nEncryption Done: A total number of {count} file(s) were encrypted.")