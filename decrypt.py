import os 
from cryptography.fernet import Fernet

protected_files = ["encrypt.py","decrypt.py","encryption_key.key","venv"]
target_files=["sample_image.jpg"]

# Determing files to decrypt


# Fetching the Encryption/Decryption Key (Password to allow decryption)

with open("encryption_key.key","rb") as encryption_key_object:
	encryption_key = encryption_key_object.read()
fernet_instance = Fernet(encryption_key)
count=0
# Decryption Process
for file in target_files:
	count += 1
	print(f"\nReading File #{count}: {file}")
	with open(file,"rb") as file_object:
		encrypted_content = file_object.read()
	decrypted_content = fernet_instance.decrypt(encrypted_content)

	with open(file,"wb") as file_object:
		file_object.write(decrypted_content)
	print(f"Decrypted '{file}'")
print(f"\nDecryption Done: A total number of {count} file(s) were decrypted.")