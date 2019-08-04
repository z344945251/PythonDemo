

# try-catch
def try_catch():
    lt = [1, 2]
    try:
        1/0
    except IndexError:
        print("异常")
    except Exception as e:
        print("2",e)


# try/except/else
def try_catch_else():
    try:
        1/1
    except IndexError:
        print("异常")
    else:
        print("no exception")


# try/Except/finally
def try_catch_finally():
    try:
        1/0
    except ZeroDivisionError:
        print("异常")
    finally:
        print("try is done")


def safe_integer_input(prompt):
    input_str = input(prompt)
    try:
        number = int(input_str)
        return number
    except ValueError as ve:
        print("error: ",ve)
        print("Error in number format:", input_str)
        return safe_integer_input(prompt)


# raise抛出异常
def raise_exception():
    a = 0
    if a == 0:
        raise Exception("a must not be zero")


if __name__ == "__main__":
    raise_exception()