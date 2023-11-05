import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

csv_writer = csv.writer(open('csv', 'w+'))

page_url = 'http://www.codeabbey.com/index/user_ranking'
req = Request(page_url)
req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
html = urlopen(req).read()
parsed = BeautifulSoup(html, 'html.parser')


for tr in parsed.find_all('tr', class_='centered none')[0:]:
    tds = tr.find_all('td')
    csv_writer.writerow([tds[0].text, tds[2].find('a').text, tds[4].find('span').text, tds[5].text, tds[6].text])
