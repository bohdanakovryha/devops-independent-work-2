def check_string(value):
    if not isinstance(value, str):
        raise TypeError(f"expected str, got {type(value).__name__}")


def print_string(text):
    try:
        check_string(text)
    except TypeError as error:
        print(f"Error: {error}")
        return None
    print(text)
    return text


def describe_case(word):
    try:
        check_string(word)
    except TypeError as error:
        print(f"Error: {error}")
        return None
    letters = [ch for ch in word if ch.isalpha()]
    if not letters:
        result = "no letters"
    elif all(ch.isupper() for ch in letters):
        result = "all uppercase"
    elif all(ch.islower() for ch in letters):
        result = "all lowercase"
    else:
        result = "mixed case"
    print(f"'{word}': {result}")
    return result


def upper_letters(word):
    try:
        check_string(word)
    except TypeError as error:
        print(f"Error: {error}")
        return None
    return [ch.upper() for ch in word]