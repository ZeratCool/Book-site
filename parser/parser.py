import os

import lxml
import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup
import pandas as pd



class Product_parser:
    def __init__(self, url):
        self.base_url = url
        self.visited_urls = set()
        self.data = []
        self.download_dir = 'books'
        os.makedirs(self.download_dir, exist_ok=True)

    def product_parser(self, url):
        respone = requests.get(url).text.strip()
        soup = BeautifulSoup(respone, 'lxml')
        title = soup.find('h1', class_='book-meta__title').text.strip()
        author = soup.find('span', itemprop='author').text.strip()
        category = soup.find('div', class_='book-meta__category').text.strip().split(':')[1].strip()
        date = soup.find('div', class_='book-meta__year').find('div', class_='book-meta__value').text.strip()

        annotation_div = soup.find('div', class_='book-annotation__text')
        annotation = annotation_div.text.strip() if annotation_div else None

        #               ===IMAGE SAVING===
        image_url = soup.find('img', itemprop='image')['src']
        image_name = os.path.basename(image_url)
        image_path = os.path.join('images', image_name)
        with open(image_path, 'wb') as image_file:
            image_response = requests.get(image_url)
            image_file.write(image_response.content)
        # ===========================================

        #            === DOWNLOAD FILE ===
        book_section = soup.find('a', class_='download-links__icon download-links__icon--fb2')

        link = book_section['href']
        file_name = os.path.basename(link)

        book_response = requests.get(link)

        book_path = os.path.join(self.download_dir, file_name)
        with open(book_path, 'wb' ) as book_file:
            book_file.write(book_response.content)


        self.data.append({
            'Title': title,
            'Author': author,
            'Category': category,
            'Date': date,
            'Annotation': annotation,
            'Image Path': image_path,
            'Book Path': book_path
        })









    def parse_website(self):
        self.page_parser(self.base_url)
        self.write_to_csv()


    def page_parser(self, url):
        response = 'https://limbook.net' + requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        lst = []
        page_links = soup.find_all('a', class_='book-link')


        for i in page_links:
            product = i['href']
            self.product_parser(product)

        next_page = soup.find('a', rel='next')
        if next_page:
            next_page_url = next_page['href']
            if next_page_url in self.visited_urls:
                return
        self.visited_urls.add(next_page)

        self.page_parser(next_page_url)

    def write_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv('books_data.csv', index=False)


if __name__ == '__main__':
    web_url = 'https://limbook.net/books/'
    parser = Product_parser(web_url)
    # parser.parse_website()
