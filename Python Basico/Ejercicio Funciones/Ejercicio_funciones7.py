def is_prime(num1):
    if num1 <= 1:
        return False  # 1, 0 y los números negativos no son primos

    is_prime_result = True
    for divisor in range(2, num1):
        if num1 % divisor == 0:
            is_prime_result = False
    return is_prime_result


def get_primes(list_of_numbers):
    num_primos = []
    for number in list_of_numbers:
        if is_prime(number):
            num_primos.append(number)
    return num_primos


main_list = [1, 4, 6, 7, 13, 9, 67]
result = get_primes(main_list)
print(result)
