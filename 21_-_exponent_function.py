# Function that raises base number to a provisional power is defined by the following block of code.
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))
