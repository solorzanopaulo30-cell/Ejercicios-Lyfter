
list_a = ["Email", "Born Year"]
user = {"Name": "Aleks", 
        "Last Name": "Castillo", 
        "Email": "aleks.castillo@gmail.com",
        "Born Year": int("2000")}


for info in list_a:
    user.pop(info)
print(user)