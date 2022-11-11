from bs4 import BeautifulSoup
import requests
import csv

def write_to_csv(data):
   with open('Kivano_Mobile.csv', 'a') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow((data['Название'],
                       data['Цена'],
                       data['Фото']))

def prepare_csv():
    with open('Kivano_Mobile.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('Название', 'Цена', 'Ссылку на фото'))


def get_html(url):
   responce =  requests.get(url)
   return responce.text

def get_total_pages(html):
   soup = BeautifulSoup(html, 'html.parser')
   pages_ul = soup.find('div', class_= 'pager-wrap').find('ul')
   pages_a = pages_ul.find_all('li')
   last_page = pages_ul.find_all('li')[-1]
   total_pages = last_page.find('a').get('href').split('=')[-1]
   return(int(total_pages))

def get_page_data(html):
   soup = BeautifulSoup(html, 'html.parser')
   product_list = soup.find('div', class_='list-view').find('div', class_='item product_listbox oh')
   products = soup.find_all('div', class_='item product_listbox oh')
   for product in products:
      try:
         photo = product.find('div', class_='listbox_img pull-left').find('a').find('img').get('src')
         link = 'https://www.kivano.kg' + photo
      except:
         photo = 'Нет фото!'
      try:
         title = product.find('div', class_='listbox_title oh').find('a').text
      except:
         title = 'Нет название!'
      try:
         price = product.find('div', class_='listbox_price text-center').find('strong').text
      except:
         price = 'Нет цена!'

      data = {'Фото': link, 'Название': title, 'Цена': price}
      write_to_csv(data)

   
def main():
    prepare_csv()
    mobile_url = 'https://www.kivano.kg/mobilnye-telefony'
    pages = '?page='
    get_total_pages(get_html(mobile_url))
    get_page_data(get_html(mobile_url))
    total_pages = get_total_pages(get_html(mobile_url))

    for page in range(1, total_pages+1):
       url_with_page =  mobile_url + pages + str(page)
       html = get_html(url_with_page)
       get_page_data(html)
main()