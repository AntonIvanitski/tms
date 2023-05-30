
def factorial(input_):
    elem = 1
    for i in range(1, input_+1):
        elem *= i
    return elem
print(factorial(int(input('Введите число...'))))
def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n - 1)
print(fact_recursive(int(input())))