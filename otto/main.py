from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from win10toast import ToastNotifier
import sys

url = 'https://www.otto.de/sale/deal-des-tages/'

# open connection, grabbing page
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
try:
    discount_box = page_soup.findAll("div", {"class": "benefit-main"})[0]
    discount_container = discount_box.findAll("span", {"class": "benefit-main__linkLayer"})

    discount = ""
    for container in discount_container:
        if "15€  für Neukunden" not in str(container.text.strip().replace("\n", " ").replace("\t", " ")):
            discount += str(container.text.strip().replace("\n", " ")).replace("\t", " ") + "\n"

    # Notify  it!
    if len(sys.argv) > 1 and sys.argv[1] == "notify":
        notifier = ToastNotifier()
        notifier.show_toast("Otto discount!", discount, duration=10)
    else:
        print(discount)
except:
    print("No Deals")