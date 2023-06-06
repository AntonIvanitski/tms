palindrome_tuple = ('потоп', 'тут', 'дерево')
palindrome_func = filter(lambda x: x == x[::-1], palindrome_tuple )
print(tuple(palindrome_func))