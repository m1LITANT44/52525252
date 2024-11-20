with open("supplier_b_import.txt", "r", encoding="utf-8") as file:
    for line in file:
        row = line.strip().split(',')
        lines = file.readlines()
    for line in lines:
        row = line.strip().split(',')
        print(row)

