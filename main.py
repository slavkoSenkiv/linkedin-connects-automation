# Mar23 - 15
# Mar24 - 28
# <editor-fold desc="pre code">
import random
import re
from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.keys import Keys
# <editor-fold desc="mac paths">
path_to_webdriver = '/Users/ysenkiv/Code/access files/chromedriver'
li_credentials_path = '/Users/ysenkiv/Code/access files/personal/linkedin/linkedin auth.txt'
screen_xy = [958, -41, 530, -367] # My Dell screen - 1st two = scroll xy |  2d two  = next button xy

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
# </editor-fold>
# <editor-fold desc="login">
with open(li_credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    email = lines[0].strip()
    password = lines[1].strip()

browser = webdriver.Chrome(executable_path=path_to_webdriver)
browser.get(li_login_url)
browser.find_element_by_id('username').send_keys(email)
browser.find_element_by_id('password').send_keys(password)
browser.find_element_by_xpath(login_b_xpath).click()
print('successfully logged in')
# </editor-fold>
connect_note = "I see you have game dev LiveOps related position, me too! Would you like to connect? " \
               "From time to time I'm posting stuff that I found useful for my role."
# </editor-fold> # pre code


def send_connect(name=''):
    browser.find_element_by_xpath(add_note_b_xpath).click()
    browser.find_element_by_name('message').send_keys(f'Hey {name}! {connect_note}')
    time.sleep(random.uniform(2.1, 3.1))
    browser.find_element_by_xpath(send_note_b_xpath2).click()


send_connects = 0
page_num = 1
browser.get(search_url)

while send_connects <= 30:
    print('page', page_num)
    time.sleep(2)
    connect_buttons_lst = browser.find_elements_by_xpath(connect_b_xpath)
    for connect_button in connect_buttons_lst: # sending connects on the page
        connect_button.click()

        try:
            person_name = browser.find_elements_by_xpath(add_note_offer_xpath)[0].text.split(' ')[-2]
            send_connect(person_name)

        except IndexError:
            send_connect()

        send_connects += 1
        print(f'connects send {send_connects}')
    time.sleep(random.uniform(2, 3))
    for x in range(3):
        pyautogui.click(x=screen_xy[0], y=screen_xy[1])
        time.sleep(0.5)
    pyautogui.click(x=screen_xy[2], y=screen_xy[3])
    page_num += 1


