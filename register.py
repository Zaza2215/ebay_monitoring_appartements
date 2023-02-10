#! # -*- coding: UTF8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import fake_useragent
import os
import time
import random
from config import MAIL, PASSWORD
from main import monitoring

data = {
    'message': '''
    Hello,
    My name is Pasha.
    ''',
    'call_back': True,
    # choose: ('', 'NOT_SPECIFIED', 'FEMALE', 'MALE', 'DIVERS')
    'sex': 'MALE',
    'name': 'Pasha',
    'surname': 'Kozachenko',
    'phone_number': '+380666666666',
    'street_number': '49',
    'post': ['', ''],
    # choose: ('', 'NOT_SPECIFIED', 'AVAILABLE', 'NOT_AVAILABLE')
    'info': 'NOT_SPECIFIED',
}

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
executable_path = os.path.join(MAIN_DIR, 'chromedriver', 'chromedriver.exe')
s = Service(executable_path=executable_path)
options = webdriver.ChromeOptions()

options.add_argument(
    'user-agent=Mozilla/109.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko)'
    ' Chrome/109.0.203.2 Safari/532.0')

# region: uncomment if you need random useragent
# user_agent
# user_agent = fake_useragent.UserAgent().random
# options.add_argument(f'user-agent={fake_useragent}')
# endregion

# other options
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=s, options=options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})

try:
    driver.get('https://www.ebay-kleinanzeigen.de/m-meine-anzeigen.html')
    time.sleep(2)

    try:
        driver.find_element(By.ID, "gdpr-banner-accept").click()
    except Exception as ex:
        print(ex)

    # region authorisation
    email_input = driver.find_element(By.ID, 'login-email')
    email_input.clear()
    email_input.send_keys(MAIL)

    password_input = driver.find_element(By.ID, 'login-password')
    password_input.clear()
    password_input.send_keys(PASSWORD)
    input('Waiting for passing the robot-test\nPress Enter if you pass...')

    try:
        driver.find_element(By.ID, 'login-submit').click()
    except Exception as ex:
        print(ex)

    # endregion

    time.sleep(3)


    def send_message(url_appartement: str):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url_appartement)
        time.sleep(3)

        driver.find_element(By.ID, 'viewad-contact-button').click()
        time.sleep(3)

        try:
            message = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div/form/section/fieldset/div[1]/div/textarea')
            message.clear()
            message.send_keys(data['message'])
            time.sleep(0.1)
        except:
            print('These is not message input')

        try:
            if data['call_back']:
                call_back = driver.find_element(By.ID, 'phoneCallDesired')
                call_back.click()
            time.sleep(0.1)
        except:
            print('These is not call_back checkbox')

        try:
            if data['sex']:
                info_dropdown = Select(
                    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/section/fieldset/div[4]/div/select'))
                info_dropdown.select_by_value(data['sex'])
        except:
            print('These is not sex dropdown')

        try:
            full_name = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div/form/section/fieldset/div[3]/div/input')
            full_name.clear()
            full_name.send_keys(data['name'] + ' ' + data['surname'])
            time.sleep(0.1)
        except:
            print('There is not full name input')

        try:
            name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/section/fieldset/div[5]/div/input')
            name.clear()
            name.send_keys(data['name'])
            time.sleep(0.1)
        except:
            print('These is not name input')

        try:
            surname = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/section/fieldset/div[6]/div/input')
            surname.clear()
            surname.send_keys(data['surname'])
            time.sleep(0.1)
        except:
            print('These is not surname input')

        try:
            phone_number = driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/form/section/fieldset/div[7]/div/input')
            phone_number.clear()
            phone_number.send_keys(data['phone_number'])
            time.sleep(0.1)
        except:
            print('These is not phone number input')

        try:
            phone_number = driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/form/section/fieldset/div[4]/div/input')
            phone_number.clear()
            phone_number.send_keys(data['phone_number'])
            time.sleep(0.1)
        except:
            print('These is not phone number input')

        try:
            street_number = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div/form/section/fieldset/div[8]/div/input')
            street_number.clear()
            street_number.send_keys(data['street_number'])
            time.sleep(0.1)
        except:
            print('These is not street number input')

        try:
            post = [
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/form/section/fieldset/div[9]/div/div[1]/input[1]'),
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/form/section/fieldset/div[9]/div/div[1]/input[2]')]
            post[0].send_keys(data['post'][0])
            post[1].send_keys(data['post'][1])
            time.sleep(0.1)
        except:
            print('These is not post inputs')

        try:
            if data['info']:
                info_dropdown = Select(
                    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/section/fieldset/div[10]/div/select'))
                info_dropdown.select_by_value(data['info'])
        except:
            print('These is not info dropdown')

        time.sleep(1)
        send_data = False
        try:
            send_data = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/section/fieldset/div[12]/button')
        except:
            print('THERE IS NO SEND_DATA BUTTON 1')

        try:
            send_data = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/section/fieldset/div[6]/button')
        except:
            print('THERE IS NO SEND_DATA BUTTON 2')

        # if send_data: send_data.click()
        input()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        print('-' * 20)


    while True:
        for url in monitoring():
            send_message(url_appartement=url)
            time.sleep(2)
        time.sleep(20 + random.random() * 30)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
