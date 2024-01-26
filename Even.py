
def sum_of_even_numbers(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

result = sum_of_even_numbers(numbers)

print(f"Sum of even numbers: {result}")
