# Самостійна робота №2, групи ПДМ-51, студентки Гуленко Богдани

String functions, a generator and unit tests in Python.

## Project structure

```
src/
    __init__.py
    string_utils.py   string functions with type validation
    generator.py      even/odd generator
    examples.py       usage examples
tests/
    __init__.py
    test_string_utils.py
    test_generator.py
```

## Functions

- `print_string(text)` prints a string to the console.
- `describe_case(word)` prints whether all letters of the word are uppercase, lowercase or mixed.
- `upper_letters(word)` returns a list of the word's letters in uppercase (list comprehension).
- `even_odd_generator(limit=None)` yields "Even" and "Odd" alternately.

If a string function receives a value that is not a `str`, it prints an error message and returns `None`.

## Running the examples

```bash
python -m src.examples
```

## Running the tests

```bash
python -m unittest discover -v
```

## Git branches and versions

- `feature/functions` - string functions
- `feature/generator` - generator and examples
- `tests` - unit tests
- `v0.1` - string functions and generator
- `v0.2` - unit tests added