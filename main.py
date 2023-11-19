text = "пример для подсчета гласных букв"
f = 0
for i in text:
    if i == 'а' or i == 'е' or i == 'и' or i == 'о' or i =='ы' or i == 'у' or i == 'я':
        f += 1
print(f)
