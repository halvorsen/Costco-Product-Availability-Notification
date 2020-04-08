Costco Product Availability Notification - with Selenium

Purpose: Find when a product is available and get email notification.

Instructions (not exhaustive instructions, previous experience with python, terminal, etc required):

Feel free to contribute and create a pull request

Download Selenium Python SDK and choice of driver (I used Chrome), https://pypi.org/project/selenium/

Allow less secure app access your gmail account: https://support.google.com/accounts/answer/6010255 to use smtplib

fill in email and password info in costco.py

Open a browser to costco.com and use your zip code to enter correct store to search. you can close this browser because the zip is cached

in terminal run to test: python3 costco.py

add cron job as described in that file

common errors:

screensaver, energy effient mode, sleep mode stops the cron jobs. Solution: adjust your settings and keep your device plugged in
