dict_ = {'key1': 'value1', 'key2': 'value2'}
dict_2 = {}
for key, value in dict_.items():
    dict_2[value] = key
print(dict_2)