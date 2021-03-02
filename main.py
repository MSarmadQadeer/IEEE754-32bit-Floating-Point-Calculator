def binary_to_decimal(binary_num):
    """
    It will convert binary number to decimal
    :param binary_num:
    :return decimal_num:
    """
    decimal_num = 0
    power = binary_num.index(".") - 1 if binary_num.find(".") != -1 else len(binary_num) - 1
    for i in binary_num:
        if i == ".":
            continue
        decimal_num += int(i) * 2 ** power
        power -= 1
    return decimal_num


def decimal_to_binary(decimal_num):
    """
    It will convert decimal number to binary
    :param decimal_num:
    :return binary_num:
    """
    int_decimal = int(decimal_num)
    fraction_decimal = decimal_num - int_decimal
    int_binary = ""
    while int_decimal != 0:
        int_binary = str(int_decimal % 2) + int_binary
        int_decimal = int(int_decimal / 2)
    fraction_binary = ""
    while fraction_decimal != 0:
        fraction_decimal *= 2
        int_part = int(fraction_decimal)
        fraction_decimal -= int_part
        fraction_binary += str(int_part)

    binary_num = int_binary if fraction_binary.find("1") == -1 else f"{int_binary}.{fraction_binary}"
    return binary_num


def decimal_to_floating_point(decimal_num):
    """
    It will convert decimal number to floating point
    :param decimal_num:
    :return sign, exponent, mantissa:
    """
    sign = "1" if decimal_num[0] == "-" else "0"
    decimal_num = float(decimal_num[1:]) if sign == "1" else float(decimal_num)
    binary = decimal_to_binary(decimal_num)
    point_index = binary.find(".") if binary.find(".") != -1 else len(binary)
    first_one_index = binary.find("1")
    exponent = 127
    if first_one_index == -1:  # e.g: 0 / 0.0
        exponent = 0
    elif first_one_index < point_index:  # e.g: 10110.0101 / 1.01010110
        exponent += (point_index - (first_one_index + 1))
    elif first_one_index > point_index:  # e.g: 0.00101
        exponent += (point_index - first_one_index)
    mantissa = ""
    if exponent >= 127:  # e.g: 10110.0101 / 1.01010110
        mantissa += binary[first_one_index + 1: point_index] + binary[point_index + 1:]
    elif 127 >= exponent > 0:  # e.g: 0.00101
        mantissa += binary[first_one_index + 1:]
    else:
        mantissa += "0" * 23
    mantissa = mantissa + "0" * (23 - len(mantissa)) if len(mantissa) < 23 else mantissa[0:23]
    exponent = decimal_to_binary(exponent)
    exponent = "0" * (8 - len(exponent)) + exponent

    return sign, exponent, mantissa


def floating_point_to_decimal(floating_point):
    """
    It will convert floating point to decimal number
    :param floating_point:
    :return decimal_num:
    """
    sign = "+" if floating_point[0] == "0" else "-"
    exponent = floating_point[1:9]
    exponent = binary_to_decimal(exponent) - 127 if exponent.find("1") != -1 else 0
    mantissa = "1." + floating_point[9:] if exponent != 0 else "0"
    decimal_num = float(sign + str(binary_to_decimal(mantissa) * 2 ** exponent))
    return decimal_num


def main():
    print("\n<-- This is a Floating Point Representation System -->")
    print("|   IEE 754 32-bit Floating Point Convertor          |\n")
    flow = True
    while flow:
        try:
            binary_array = decimal_to_floating_point(input("Kindly Enter A Decimal Number: "))
            print("\nBelow is the Decimal to Floating Point Conversion:")
            print(f"SIGN | EXPONENT | MANTISSA")
            print(f"{binary_array[0]}    | {binary_array[1]} | {binary_array[2]}\n")
            print("Now converting the above floating point back to Decimal:")
            print(floating_point_to_decimal(f"{binary_array[0]}{binary_array[1]}{binary_array[2]}"))
        except:
            print("Not A Number _ Kindly Enter the Valid Input")

        print("")
        repeater = input("Reply 'yes' or 'y' to continue: ").lower()
        flow = True if repeater == "yes" or repeater == "y" else False


main()
