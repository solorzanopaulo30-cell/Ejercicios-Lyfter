
nums = [10, 20, 30, 40, 50]
average = sum(nums) / len(nums)

if average > 0:
    biggest_average = [num for num in nums if num > average]

print("Lista original:", nums)
print("Promedio:", average)
print("Valores mayores al promedio:", biggest_average)