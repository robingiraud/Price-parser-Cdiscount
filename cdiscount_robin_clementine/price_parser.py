import urllib.request as req
import urllib.parse as parser
import re

def parse_price(sku):
    if (isinstance(sku, str)):
        url = 'https://www.cdiscount.com/f-0-' + sku + '.html'
        values = {'s': 'basics','submit': 'search'}
        data = parser.urlencode({'s': 'basics','submit': 'search'}).encode('utf8')
        request = req.Request(url, data)
        response = req.urlopen(request)
        responseData = response.read()
        prices = re.findall(r'"price":(.*?),', str(responseData))

        return float(prices[0])
    else:
        return 'Wrong type of ID. It must be a string'
