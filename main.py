from bs4 import BeautifulSoup
import fake_useragent
import requests
import time
import random


def get_list_url(user_agent=fake_useragent.UserAgent().random):
    house_urls = []

    base_url = 'https://www.ebay-kleinanzeigen.de'
    url = base_url + '/s-wohnung-mieten/hamburg/c203l9409'

    headers = {
        'user-agent': user_agent,
    }
    response = requests.get(url=url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    houses_ul = html_soup.find('ul', id='srchrslt-adtable')
    houses = houses_ul.find_all('li', class_='ad-listitem lazyload-item')

    for i, house in enumerate(houses):
        try:
            house_urls.append(base_url + house.find('a', class_='ellipsis', href=True)['href'])
        except Exception as ex:
            print(ex)

    return house_urls


def monitoring() -> list:
    house_urls = get_list_url()
    print('New list:', len(house_urls), house_urls)

    with open('urls.txt', 'r', encoding='utf-8') as file:
        house_urls_old = file.read().splitlines()

    print('Old list:', len(house_urls_old), house_urls_old)

    new_houses = []
    for house_url in house_urls:
        if house_urls_old[0] == house_url:
            break
        else:
            new_houses.append(house_url)

    if len(new_houses) != 0:
        print('--- NEW HOUSE ---')
        print(new_houses)

    with open('urls.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(house_urls))

    print('\n')
    return new_houses


if __name__ == '__main__':
    # while True:
    #     monitoring()
    #     time.sleep(20 + random.random() * 30)
    import os
    MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
    print(os.path.join(MAIN_DIR, 'chromedriver', 'chromedriver.exe'))
