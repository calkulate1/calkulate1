shopping_list = ["яблоко", "молоко", "хлеб", "яйца", "сок"]

for person in shopping_list:
    print(person)
del shopping_list[1]
shopping_list[0] = 'банан'
print(shopping_list)
a = len(shopping_list)
print(a)