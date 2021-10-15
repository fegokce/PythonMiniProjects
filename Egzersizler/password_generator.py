import secrets
import string

length = secrets.choice(range(15,25))

symbols = string.ascii_letters + string.digits + string.punctuation

password = "".join(secrets.choice(symbols) for i in range(length))

print("New Password: " + password)