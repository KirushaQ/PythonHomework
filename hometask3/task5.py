last_res = 'None'


def remember_result(function_to_decorate):
    def wrapper(*args):
        global last_res
        print("Last result = " + last_res)
        last_res = function_to_decorate(*args)
    return wrapper


@remember_result
def sum_of_numbers(a, b):
    print("Current result = " + str(a+b))
    return str(a+b)


sum_of_numbers(5, 10)
sum_of_numbers(4, 8)
sum_of_numbers(1, 6)
