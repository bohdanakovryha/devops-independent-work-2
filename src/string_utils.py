def print_string(text):
    print(text)


def describe_case(word):
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
    return [ch.upper() for ch in word]