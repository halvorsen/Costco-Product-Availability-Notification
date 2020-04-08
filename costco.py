#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

browser = webdriver.Chrome()

product_pages = [
'https://www.costco.com/cottonelle-ultra-comfort-care-toilet-paper%2c-36-rolls.product.100465152.html',
'https://www.costco.com/savanna-honey-roasted-mix-nuts,-30-oz,-2-pack.product.100312634.html'



]

browser.implicitly_wait(2)


#EMAIL
def sendEmail(items):
    msg = MIMEMultipart()
    message = 'Costco Items Available:' + items
    msg["Subject"] = "Costco Availability Alert"
    msg["From"] = "first.last@domain.com"
    msg["To"] = "first.last@domain.com"
    password = "32rnSDnw3"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

#CHECK AND SEND EMAIL
def listToString(s):
    str1 = " "
    return (str1.join(s))

def checkAndSendEmail():
    availableItems = []
    for page in product_pages:
        browser.get(page)
        buyButton = browser.find_element_by_id('add-to-cart-btn')
        if buyButton.get_attribute('value') == 'Out of Stock':
            print(page)
            print('out of stock')
        else:
            print(page)
            print('in stock')
            availableItems.append(page)
    if len(availableItems) > 0:
        sendEmail(listToString(availableItems))
        
checkAndSendEmail()
browser.close()
