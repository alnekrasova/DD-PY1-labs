size = 1.44
str = 100
stroka = 50
simv = 25
size_simv = 4

new_size = size*1024*1024

book = str*stroka*simv
size_book = book*size_simv
number = new_size//size_book
result = round(number)

print("Количество книг, помещающихся на дискету:", result)
