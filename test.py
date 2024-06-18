import os
import time
import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import unicodedata


class Product_parser:
    def __init__(self, url):
        self.base_url = url
        self.visited_urls = set()
        self.data = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.image_dir = 'media'
        self.download_dir = 'books'
        os.makedirs(self.image_dir, exist_ok=True)
        os.makedirs(self.download_dir, exist_ok=True)

    def product_parser(self, url):
        time.sleep(random.uniform(1, 3))
        if not url.startswith('http'):
            url = 'https://limbook.net' + url  # Assuming all URLs are relative
        response = requests.get(url, headers=self.headers).text
        soup = BeautifulSoup(response, 'lxml')
        title = soup.find('h1', class_='book-meta__title').text.strip()
        author = soup.find('span', itemprop='author').text.strip()
        category = soup.find('div', class_='book-meta__category').text.strip().split(':')[1].strip()
        date_element = soup.find('div', class_='book-meta__year')
        if date_element:
            date_value = date_element.find('div', class_='book-meta__value')
            date = date_value.text.strip() if date_value else None
        else:
            date = None
        description_elem = soup.find('div', class_='book-annotation__text')
        description_parag = description_elem.find_all('p')
        description = '\n'.join([p.text.strip() for p in description_parag[:-1]]) if description_elem else None

        # Sanitize title to remove invalid characters for file name
        title = ''.join(c for c in title if c.isalnum() or c in (' ', '.', '_', '-'))

        # ===IMAGE SAVING===
        image_element = soup.find('img', itemprop='image')
        if image_element:
            image_url = image_element['src']
            if not image_url.startswith('http'):
                image_url = 'https://limbook.net' + image_url  # Assuming all URLs are relative
            image_name = title

            image_path = os.path.join(self.image_dir, image_name + '.jpg')  # Save as JPEG
            with open(image_path, 'wb') as image_file:
                image_response = requests.get(image_url)
                image_file.write(image_response.content)
        else:
            image_path = None
        # ==================

        # === DOWNLOAD FILE ===
        book_section = soup.find('a', class_='download-links__icon download-links__icon--fb2')

        if book_section:
            link = book_section['href']
            if not link.startswith('http'):
                link = 'https://limbook.net' + link  # Assuming all URLs are relative

            file_name = title + '.zip'

            book_path = os.path.join(self.download_dir, file_name)  # Save as ZIP

            # Downloading the file using requests
            with open(book_path, 'wb') as book_file:
                file_response = requests.get(link, headers=self.headers)
                book_file.write(file_response.content)

            self.data.append({
                'Title': title,
                'Author': author,
                'Category': category,
                'Date': date,
                'Annotation': description,
                'Image Path': image_path,
                'Book Path': book_path
            })
        else:
            print(f"No download link found for {title}. Skipping...")

    def parse_website(self):
        self.page_parser(self.base_url)
        self.write_to_csv()

    def page_parser(self, url):
        if not url.startswith('http'):
            url = 'https://limbook.net' + url  # Assuming all URLs are relative
        response = requests.get(url, headers=self.headers).text
        soup = BeautifulSoup(response, 'lxml')
        page_links = soup.find_all('a', class_='book-link')

        for i in tqdm(page_links, desc="Parsing pages"):
            product = i['href']
            self.product_parser(product)

        next_page = soup.find('a', rel='next')
        if next_page:
            next_page_url = next_page['href']
            if next_page_url in self.visited_urls:
                return
            self.visited_urls.add(next_page_url)
            time.sleep(random.uniform(1, 3))
            self.page_parser(next_page_url)

    def write_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv('books_data.csv', index=False)


if __name__ == '__main__':
    web_url = 'https://limbook.net/books/'
    parser = Product_parser(web_url)
    parser.parse_website()
