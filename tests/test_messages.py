from python_printer import printer


def test_print_message():
    message = "Hello Angel!"
    formatted_message = f"This is printing this: {message}"
    assert formatted_message == printer.print_this_message(message)

def test_add_message():
    num1 = 3
    num2 = 2
    formatted_message = f"Result: 5"
    assert formatted_message == printer.print_add(num1, num2)
