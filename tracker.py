from http import server
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
URL = 'https://www.amazon.com/HP-Convertible-i7-1165G7-Entertainment-15-ed1010nr/dp/B091D5QNTT'
import smtplib

import time

def track(url):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()

        page.goto(url)

        html = page.inner_html('#ppd')
        parse(html)
        
def parse(html):
    soup = BeautifulSoup(html,'html.parser')

    title = soup.find('span',id='productTitle').get_text().split(',')[0].strip()
    print(title)

    price = soup.find('span','a-offscreen').get_text().strip().replace('$','')
    price=float(price)

    if price<777.00:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.ehlo()

    server.login('evansmakuba69@gmail.com','makxtfkqmmmqafsl')
    subject = 'price went down!'

    body = f'check the amazon link {URL}'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'evansmakuba69@gmail.com',
        'makubaevansakala@gmail.com',
        msg
    )
    print("email sent")
    server.quit()

if __name__=='__main__':
    try:
        while True:
            track(URL)
            print('sleeping for an hour...')

            time.sleep(3600)
    except KeyboardInterrupt:
        print('keyboard interrupt')