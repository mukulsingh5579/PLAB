#The "Ghost" File Encryption

from cryptography.fernet import Fernet
from PIL import Image

# Generate a key and encrypt
key = Fernet.generate_key()
cipher = Fernet(key)
message = b"Top Secret: The password is 'Phoenix'"
encrypted_text = cipher.encrypt(message)

# Create a tiny 10x10 image to 'hide' the data in its metadata
img = Image.new('RGB', (10, 10), color = (73, 109, 137))
img.info['secret'] = encrypted_text

print(f"Encryption Key: {key.decode()}")
img.save('vault.png')
print("Secret message hidden in vault.png metadata!")