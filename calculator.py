from operations.addition import Addition
from operations.multiplication import Multiplication
from operations.division import Division

# Пример использования калькулятора
num1 = (3, 4)  # 3 + 4j
num2 = (1, 2)  # 1 + 2j

# Сложение
result_addition = Addition.add_complex_numbers(num1, num2)
print("Сложение:", result_addition)

# Умножение
result_multiplication = Multiplication.multiply_complex_numbers(num1, num2)
print("Умножение:", result_multiplication)

# Деление
result_division = Division.divide_complex_numbers(num1, num2)
print("Деление:", result_division)