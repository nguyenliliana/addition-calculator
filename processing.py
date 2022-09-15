import statistics


def calculate_mode(number_list):
    try:
        return "The mode of the numbers is {}".format(statistics.mode(number_list))
    except statistics.StatisticsError as exc:
        return "Error calculating mode: {}".format(exc)


def calculate_sum(number1, number2):
    return number1 + number2


def calculate_difference(number1, number2):
    return number1-number2


def calculate_product(number1, number2):
    return number1*number2


def calculate_quotient(number1, number2):
    if number2 == 0:
        return "Undefined"
    return number1/number2
