Statement = ["Staten", "Ramen", "Lisa"]
names = ["Ramen" , "Lisa", "Damen"]


for state in Statement:
    for name in names:
        if name == state:
            Statement = True
        else:
            Statement = f"Does not contain {name}"

print(Statement)
