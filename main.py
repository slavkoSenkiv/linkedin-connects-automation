#todo add contact name into connect note
#todo add next pages into cycle
#todo add random timing pause

import random
from selenium import webdriver
import time

path_to_webdriver = '/Users/ysenkiv/Code/access files/chromedriver'
li_login_url = 'https://www.linkedin.com/uas/login'
login_b_xpath = '/html/body/div/main/div[2]/div[1]/form/div[3]/button'
connect_b_xpath = "//button/span[text()='Connect']/.."
add_note_b_xpath = "//*[@class='artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view mr1']"
send_note_b_xpath = "//*[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1']"
connect_note = "Hey there! I see you have game dev LiveOps related position, me too! Would you like to connect? From time to time I'm posting stuff that I found useful for my role."
browser = webdriver.Chrome(executable_path=path_to_webdriver)
login = 'xxxxx@gmail.com'
password = 'xxxxx'
liveOps_mobile_computer_games_english='https://www.linkedin.com/search/results/people/?industry=%5B%223131%22%2C%22109%22%5D&keywords=liveops&origin=FACETED_SEARCH&profileLanguage=%5B%22en%22%5D&sid=pzM'
search_url = liveOps_mobile_computer_games_english
browser.get(li_login_url)
browser.find_element_by_id('username').send_keys(login)
browser.find_element_by_id('password').send_keys(password)
browser.find_element_by_xpath(login_b_xpath).click()
print('successfully logged in')
browser.get(search_url)
page_num = 1
person_num = 1
connect_buttons_lst = browser.find_elements_by_xpath(connect_b_xpath)
print('got connect button list')
for connect_button in connect_buttons_lst:
    connect_button.click()
    browser.find_element_by_xpath(add_note_b_xpath).click()
    browser.find_element_by_name('message').send_keys(connect_note)
    browser.find_element_by_xpath(send_note_b_xpath).click()
    print(f'page {page_num} person {person_num}')
    person_num += 1
    time.sleep(2)

