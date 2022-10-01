# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:

# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Enter number: ')) 

def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sum(sequence(n)))