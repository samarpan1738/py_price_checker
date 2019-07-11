#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import smtplib
import time
#Url to scrape
url='https://www.flipkart.com/flipkart-smartbuy-dash-series-g8-gaming-mouse/p/itmfdxfjgfwhkk98?pid=ACCFDXFJKCVD9BAV&lid=LSTACCFDXFJKCVD9BAVNCPGBK&marketplace=FLIPKART'
#Browser headers
headers={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

def get_price():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    price=soup.findAll("div", {"class": "_1vC4OE _3qQ9m1"})[0].get_text()
    price=float(price[1:])
    if(price<500.0):
        send_email()

def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    #ehlo=extended hello
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('haritsamarpan7@gmail.com','gnrxyhsrwubtfyll')

    subject='Price fell down'
    body='Check the G8 mouse @'+url
    
    msg=f"Subject:{subject}\n{body}"
    server.sendmail(
        'haritsamarpan7@gmail.com','haritsamarpan679@gmail.com',msg
    )
    print("Price dropped,Email Sent")
    server.quit()

while(True):
    get_price()
    time.sleep(86400)
