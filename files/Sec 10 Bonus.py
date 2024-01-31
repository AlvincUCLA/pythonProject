password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

#Assuming "False" first for the logistic related issues

digit = False
for i in password:
    if i.isdigit():
        digit = True

result ["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

print(all(result))
print(result.values())

if all(result) == True:
    print("Strong Password")
else:
    print("Weak Password")
    password = input("Enter another password: ")