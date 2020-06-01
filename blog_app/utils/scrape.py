from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib.request import urlretrieve
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import os

SCRAPE_DIR =''

#csv_writer.writerow(['Headline', 'Summary', 'Link', 'title', 'Content', 'Image'])



def scrape_site(web_address='https://nltimes.nl/categories/entertainment'):
    x = os.getcwd()
    os.chdir('C:/Users/feren/PycharmProjects/django_env/django_prj/media/post_images')
    csv_file = open('scraped_data.csv', 'w+', newline='')
    csv_writer = csv.writer(csv_file)
    source = requests.get(web_address).text
    soup = BeautifulSoup(source, 'lxml')
    articles = soup.find_all('div', class_='views-row')
    #print(articles[0])

    for article in articles:
        try:
            headline = article.find('h2', class_='field-content').text
            #print('Headline: ', headline)

            summary = article.find('div', class_='views-field views-field-body').text
            #print('Summary:', summary)

            article_url = article.find('h2', class_='field-content')
            re_pattern = r'([^"]*)'
            article_url = ('https://nltimes.nl' + re.findall(re_pattern, str(article_url))[6])
            #print('URL: ', article_url)

            title = article.find('div', class_='views-field-title').text
            #print('Title: ', title)

            full_source = requests.get(article_url).text
            full_soup = BeautifulSoup(full_source, 'lxml')
            full_page = full_soup.find('div', class_='field-type-text-with-summary')
            full_text = full_page.find('div', class_='field-item').text
            #print(full_text)

            image_link = full_soup.find('img', class_='image-style-main')
            image_link = image_link["src"].split("src=")[-1]
            #print(image_link)
            filename = ('%s.jpg' % (timestr+title[1:4]))
            urlretrieve(image_link, filename)
            print(filename)
            csv_writer.writerow([headline, summary, article_url, title, full_text, 'post_images/'+filename])

        except:
            continue

    csv_file.close()
    os.chdir(x)











def upload_data():
    x = os.getcwd()
    os.chdir('C:/Users/feren/PycharmProjects/django_env/django_prj/media/post_images')

    from blog_app.models import User
    from blog_app.models import Post
    me = User.objects.get(id=1)
    with open('scraped_data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, content = Post.objects.get_or_create(title=row[0], author=me, content=row[4], image=row[5])
    os.chdir(x)

