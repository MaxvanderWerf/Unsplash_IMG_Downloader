import selenium
import urllib
import struct
import ctypes
import random
from selenium import webdriver
from urllib.request import urlretrieve
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

DRIVER_PATH = r'C:\Users\max_v\Desktop\Scraping\chromedriver'
wd = webdriver.Chrome(executable_path=DRIVER_PATH)

wd.get('https://unsplash.com')

# Themes to search for on unsplash.com
subjects = ['Football', 'The Netherlands', 'Peru', 'Nature', 'Abstract', 'Animals']
search_term = random.choice(subjects)

search_box = wd.find_element_by_css_selector('#SEARCH_FORM_INPUT_homepage-header-big')
search_box.send_keys(search_term)
search_box.submit();

# Wait in case the website is a bit slow
element = WebDriverWait(wd, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(2) > figure > div > div:nth-child(2) > div > div"))
    )

images = wd.find_elements_by_tag_name('img')

list = []
for image in images:
    list.append(image.get_attribute('src'))

# Making sure I only download photos and not the profile pics of artists
photos = [url for url in list if 'photo' in url] 

# Downloading the photos
for i in range(len(photos)):
    url = photos[i]
    path = f'C:/Users/max_v/Downloads/OneDrive/Pictures/Backgrounds/Unsplash/IMG{i}.jpg'
    urlretrieve(url, path)

wd.close()

# Setting a horizontal photo as background
for i in range(len(photos)):
    SPI_SETDESKWALLPAPER = 20
    with Image.open(f'C:/Users/max_v/Downloads/OneDrive/Pictures/Backgrounds/Unsplash/IMG{i}.jpg') as img:
        width, height = img.size
    PATH = f'C:/Users/max_v/Downloads/OneDrive/Pictures/Backgrounds/Unsplash/IMG{i}.jpg'
    while width > height:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
        break
