import email.message
import smtplib

import requests
from bs4 import BeautifulSoup

url = 'https://store.playstation.com/pt-br/product/UP9000-CUSA34384_00-GOWRAGNAROK00000'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_ = 'psw-m-b-5 psw-t-title-l psw-t-size-8 psw-l-line-break-word').getText()
price = soup.find('span', class_='psw-t-title-m').getText()

num_price = price[2:]
num_price = num_price.replace(',', '.')
num_price = float(num_price)

def send_email():

    corpo_email = '''
    https://store.playstation.com/pt-br/product/UP9000-CUSA34384_00-GOWRAGNAROK00000
    '''

    msg = email.message.Message()
    msg['Subject'] = 'God of War no preço acessível'
    msg['From'] =  'pypazabo@gmail.com'
    msg['To'] = 'pypazabo@gmail.com'
    password = 'nugawczhpeybxgcq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email Enviado')



if (num_price <= 240):
    send_email()