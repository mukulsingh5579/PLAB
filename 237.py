#Email Slicer (Extract Username & Domain)
email = input("Enter email: ")

username = ""
domain = ""

for i in range(len(email)):
    if email[i] == "@":
        username = email[:i]
        domain = email[i+1:]

print("Username:", username)
print("Domain:", domain)