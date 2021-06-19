def print_this_message(message: str):
    formatted_message = f"This is printing this: {message}"
    print(formatted_message)
    return formatted_message

def print_add(num1: int, num2: int):
    res = num1 + num2
    formatted_message = "Result: {}".format(str(res))
    print(formatted_message)
    return formatted_message