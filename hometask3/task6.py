last_res = 0


def call_once(function_to_decorate):
    def wrapper(*args):
        global last_res
        if last_res == 0:
            function_to_decorate(*args)
        last_res = 1
    return wrapper


@call_once
def sum_of_numbers(a, b):
    print(a+b)
    return a+b


sum_of_numbers(5, 10)
sum_of_numbers(4, 8)
sum_of_numbers(1, 6)