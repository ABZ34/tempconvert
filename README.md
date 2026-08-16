# tempconvert

A tiny command-line tool for converting temperatures between Celsius, Fahrenheit, and Kelvin.

## Usage

```bash
python tempconvert.py <value> <from_unit> <to_unit>
```

`from_unit` and `to_unit` are one of `c`, `f`, `k`.

### Examples

```bash
python tempconvert.py 100 c f
# 100.0C = 212.00F

python tempconvert.py 32 f c
# 32.0F = 0.00C

python tempconvert.py 0 c k
# 0.0C = 273.15K
```

## Running tests

```bash
python -m unittest
```
