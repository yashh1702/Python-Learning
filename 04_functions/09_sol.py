# Yield ek aisa function hai jo value ko generate krta hai aur return krta hai aur memory mai be store krta hai jisse ki next vo wahi hai access ho sakhe aur hume value mil sakhe

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)