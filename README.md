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

print(parse_price('<SKU>'))
```

You can find any product's SKU in the product page URL.

## Web app
A litte user interface is included to this project

To use it, you need to have Node.js and NPM installed : [npm](https://www.npmjs.com/get-npm)
Go to /parser-app with command line tool and run :
```bash
npm install
```
then :
```bash
npm run serve
```
Don't forget :
```bash
pip install flask_cors
```

Finally: run flask server :
```bash
env FLASK_APP=server.py flask run
```

Go to : [localhost](localhost:8080)

And you can enjoy!


## License
Copyright (c) 2018 The Python Packaging Authority
