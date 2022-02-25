from itertools import product
from time import sleep
from requests_html import HTMLSession

url = 'https://www.trustpilot.com/categories/electronics_technology'

s = HTMLSession()
r = s.get(url)

# print(r.status_code)
product = r.html.xpath('//*[@id="__next"]/div/main/div/div[2]/section/div[2]/div[2]', first=True)
# print(product.absolute_links)
for item in product.absolute_links:
    r = s.get(item)
    print(r.html.find('h1.typography_typography__QgicV span', first=True).text)