"""Simple command-line temperature converter."""

import argparse
import sys


def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius):
    return celsius + 273.15


def k_to_c(kelvin):
    return kelvin - 273.15


def f_to_k(fahrenheit):
    return c_to_k(f_to_c(fahrenheit))


def k_to_f(kelvin):
    return c_to_f(k_to_c(kelvin))


CONVERSIONS = {
    ("c", "f"): c_to_f,
    ("f", "c"): f_to_c,
    ("c", "k"): c_to_k,
    ("k", "c"): k_to_c,
    ("f", "k"): f_to_k,
    ("k", "f"): k_to_f,
}


def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit == to_unit:
        return value
    key = (from_unit, to_unit)
    if key not in CONVERSIONS:
        raise ValueError(f"Unsupported conversion: {from_unit} -> {to_unit}")
    return CONVERSIONS[key](value)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Convert a temperature between C, F, and K.")
    parser.add_argument("value", type=float, help="Temperature value to convert")
    parser.add_argument("from_unit", choices=["c", "f", "k"], help="Unit to convert from")
    parser.add_argument("to_unit", choices=["c", "f", "k"], help="Unit to convert to")
    args = parser.parse_args(argv)

    result = convert(args.value, args.from_unit, args.to_unit)
    print(f"{args.value}{args.from_unit.upper()} = {result:.2f}{args.to_unit.upper()}")


if __name__ == "__main__":
    sys.exit(main())
