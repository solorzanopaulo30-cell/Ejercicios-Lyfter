#3. Cree un programa que reciba 3 números y muestre cuál es el mayor.

def biggest(num, num2, num3):
    if num > num2 and num > num3:
        result = num
    elif num2 > num and num2 > num3:
        result = num2
    else:
        result = num3
    print(result)

biggest(5, 9, 61)

def biggest_num(num, num2, num3):
    result = max(num, num2, num3)
    print(result)

biggest_num(545,15619, 2694)