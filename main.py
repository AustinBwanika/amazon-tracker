import requests
import lxml
from bs4 import *
import smtplib as mail
import html
import os

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url=PRODUCT_URL, headers=header)
web_page = response.content

soup = BeautifulSoup(web_page, "lxml")
price = soup.find(class_="a-offscreen").get_text()
title = soup.find(id="productTitle").get_text()
title = title.encode('utf-8')
price = float(price.split("$")[1])

set_price = 1
print(title)
if set_price > price:
    with mail.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Price Drop\n\n {title} has dropped in price\n {PRODUCT_URL}")

with mail.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email,
                        msg=f"Subject:Price Drop\n\n Hello")