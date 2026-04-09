#Email Slicer (Extract Username & Domain)
email = input("Enter your email: ")

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)