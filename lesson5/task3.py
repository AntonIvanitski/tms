from  random import  randint
dict_ = {randint(1,20) for i in range(10)}
def count():
    for i in dict_:
        print(i)
count()