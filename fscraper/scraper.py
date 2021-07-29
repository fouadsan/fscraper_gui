from bs4 import BeautifulSoup
import requests
import os
import csv


def scrap(url, class_name, html_element, *args):

    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')

    path = os.path.join(os.environ["USERPROFILE"], "Downloads")

    with open(f'{path}\\scraped.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['object'])

        sources = soup.find_all('div', class_=class_name)
        for source in sources:
            if html_element == "img":
                try:
                    object = eval(f"source.{html_element}['src']")
                    print(object)
                except Exception as e:
                    object = None
            else:
                try:
                    object = eval(f"source.{html_element}.text")
                    print(object)
                except Exception as e:
                    object = None

            csv_writer.writerow([object])
