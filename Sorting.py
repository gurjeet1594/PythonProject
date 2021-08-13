number = [1, 2, 2, 5, 6, 3, 3, 7, 9, 8]
number.sort()
unique = []

for num in number:
    if num not in unique:
        unique.append(num)
print(unique)











