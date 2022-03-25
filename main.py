# Mar23 - 15
# Mar24 - 28
# Mar25 - 1
# <editor-fold desc="pre code">
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

import time
# <editor-fold desc="mac paths">
# path_to_webdriver = '/Users/ysenkiv/Code/access files/chromedriver' # Mac
path_to_webdriver = 'C://Users//slavk//root//Code//access files//chromedriver' # Dell
li_credentials_path = 'C://Users//slavk//root//Code//access files//personal//linkedin/linkedin auth.txt'
# </editor-fold>
# <editor-fold desc="urls">
li_login_url = 'https://www.linkedin.com/uas/login'
# search_url = f'https://www.linkedin.com/search/results/people/?industry=%5B%223131%22%2C%22109%22%5D&keywords=liveops&origin=FACETED_SEARCH&page={page_num}'
search_url = f'https://www.linkedin.com/search/results/people/?industry=%5B%223131%22%2C%22109%22%5D&keywords=liveops&origin=FACETED_SEARCH&sid=yBZ'
# </editor-fold>
# <editor-fold desc="xpaths">
login_b_xpath = '/html/body/div/main/div[2]/div[1]/form/div[3]/button'
connect_b_xpath = "//button/span[text()='Connect']/.."
next_page_b_xpath = "//*[@id='ember158']"
add_note_b_xpath = "//*[@class='artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view mr1']"
name_xpath = "/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[4]/div/div/button[2]"
send_note_b_xpath1 = "//*[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1']"
send_note_b_xpath2 = "/html/body/div[3]/div/div/div[3]/button[2]"
add_note_offer_xpath = "//*[@class='flex-1']"
dismiss_connect_b_xpath = "//*[@aria-label='Dismiss']"
# </editor-fold>
# <editor-fold desc="login">

with open(li_credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    email = lines[0].strip()
    password = lines[1].strip()

browser = webdriver.Chrome(executable_path=path_to_webdriver)
browser.get(li_login_url)
browser.find_element(by=By.ID, value='username').send_keys(email)
browser.find_element(by=By.ID, value='password').send_keys(password)
browser.find_element(by=By.XPATH, value=login_b_xpath).click()
print('successfully logged in')
# </editor-fold>

connect_note = "I see you have game dev LiveOps related position, me too! Would you like to connect? " \
               "From time to time I'm posting stuff that I found useful for my role."
# </editor-fold> # pre code


def send_connect(name=''):
    browser.find_element(by=By.XPATH, value=add_note_b_xpath).click()
    browser.find_element(by=By.NAME, value='message').send_keys(f'Hey {name}! {connect_note}')
    time.sleep(random.uniform(2.1, 3.1))
    try:
        browser.find_element(by=By.XPATH, value=dismiss_connect_b_xpath).click()
    except NoSuchElementException:
        browser.find_element(by=By.XPATH, value=send_note_b_xpath2).click()


send_connects = 0
page_num = 1
browser.get(search_url)

while send_connects <= 30:
    print('page', page_num)
    # connect_buttons_lst = browser.find_elements(by=By.XPATH, value=connect_b_xpath)

    try:

        connect_buttons_lst = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, connect_b_xpath)))
        print('found connect buttons', len(connect_buttons_lst))
        for connect_button in connect_buttons_lst:
            connect_button.click()

            try:
                person_name = browser.find_elements(by=By.XPATH, value=add_note_offer_xpath)[0].text.split(' ')[-2]
                send_connect(person_name)

            except IndexError:
                send_connect()

            send_connects += 1
            print(f'connects send {send_connects}')

    except TimeoutException:
            print('no connects found')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button/span[text()='Next']")))
    button.click()
    page_num += 1


