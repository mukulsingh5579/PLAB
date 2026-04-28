#Generating a Random Password
import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(12))

print(f"Your secure generated password: {password}")