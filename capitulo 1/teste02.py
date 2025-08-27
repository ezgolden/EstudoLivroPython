numbers = [10, 20, 30, 40]

print("ID da lista 'numbers':", id(numbers))

numbers_iter = iter(numbers)
print("ID do iterador 'numbers_iter':", id(numbers_iter))
print("IDs são iguais?", id(numbers) == id(numbers_iter))

print("\nMétodo __iter__ da lista:", numbers.__iter__)

print("\nConsumindo o iterador:")
print(next(numbers_iter))  # 10
print(next(numbers_iter))  # 20