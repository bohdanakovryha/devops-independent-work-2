from src.string_utils import print_string, describe_case, upper_letters
from src.generator import even_odd_generator


def main():
    print("1. print_string")
    print_string("Hello, Python!")

    print("\n2. describe_case")
    for word in ["PYTHON", "python", "PyThOn"]:
        describe_case(word)

    print("\n3. upper_letters")
    print(upper_letters("smogtether"))

    print("\n4. even_odd_generator")
    for number, label in enumerate(even_odd_generator(6), start=1):
        print(number, label)

    print("\n5. Type validation")
    print_string(123)
    describe_case(["word"])
    upper_letters(None)


if __name__ == "__main__":
    main()