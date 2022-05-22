def calculating_math_func(data):
    if data in fact:
        result = fact[data]
    else:
        result = max(fact.values())
        for index in range(max(fact.keys()) + 1, data + 1):
            result *= index
            fact[index] = result
    result /= data ** 3
    result = result ** 10
    return result


fact = {1: 1}
num = int(input('Введите число: '))
print('Результат:', calculating_math_func(num))