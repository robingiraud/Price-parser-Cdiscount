  # cdiscount_robin_clementine

cdiscount_robin_clementine is a Python library for parsing any cdiscount product price.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this package.

```bash
pip install -i https://test.pypi.org/simple/ cdiscount_robin_clementine
```

## Usage

```python
from cdiscount_robin_clementine.price_parser import parse_price

print(parse_price('<SKU>))
```

You can find any product's SKU in the product page URL.

## License
Copyright (c) 2018 The Python Packaging Authority
