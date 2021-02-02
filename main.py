from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

keyword = input("Enter the channel name.\n").title()

driver = webdriver.Chrome('/home/vishal/Downloads/chromedriver')
driver.get('https://www.youtube.com')

import time

search_bar = driver.find_element_by_name('search_query')
search_bar.clear()
search_bar.send_keys(f'{keyword} \n')
time.sleep(10)
channel_link = driver.find_element_by_id('main-link').click()
time.sleep(10)

try:
    got_it = driver.find_element_by_css_selector('#accept-button a').click()
except:
    pass

playlist = driver.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[3]/div').click()

time.sleep(20)

try:
    created_playlists = driver.find_element_by_link_text('Created playlists').click()
except:
    pass

for _ in range(10):
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 20000);")

names_of_playlists = []
for tag in driver.find_elements_by_id('video-title'):
    if tag.text == '':
        continue
    else:
        names_of_playlists.append(tag.text)

time.sleep(20)
links_of_playlists = []
for tag in driver.find_elements_by_css_selector('#view-more a'):
    links_of_playlists.append(tag.get_attribute('href'))
links_of_playlists = links_of_playlists[len(links_of_playlists)-len(names_of_playlists):]

print(len(names_of_playlists), len(links_of_playlists))
print(names_of_playlists)
print(links_of_playlists)

playlist_details = [{"playlist_name": names_of_playlists[i], "playlist_link": links_of_playlists[i]} for i in range(len(names_of_playlists))]
print(playlist_details)

import pandas
df = pandas.DataFrame(playlist_details)
print(df)
df.to_csv(f"List_of_playlists_{keyword.replace(' ','')}.csv")
