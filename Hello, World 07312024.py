Statement = ["Staten", "Ramen", "Lisa"]
names = ["Raul","Ramen", "Lisa"]

all_found = True

for name in names:
    if name not in Statement:
        print(f"Does not contain {name}")
        all_found = False

if all_found:
    print(True)
