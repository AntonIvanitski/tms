from itertools import product
list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5]
print([new_list for new_list in product(list_1,list_2)])