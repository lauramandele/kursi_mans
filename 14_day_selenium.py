from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # we might need to insert some delay in the code
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)  # set path to chromedriver if you have no PATH

url = "https://www.ss.com/"
driver.get(url)  # this will open the url in browser
time.sleep(0.2)  # this will wait for 2 seconds
cars_element = driver.find_element(By.ID, "mtd_97")  # this id is for this "C:\\Temp\\articular page
cars_element.click()
time.sleep(0.2)  # this will wait for 2 seconds

skoda_element = driver.find_element(By.ID, "ahc_158")  # this id is for this "C:\\Temp\\articular page
skoda_element.click() # atver Škodu sarakstu

head_line = driver.find_element(By.ID, "head_line") # dabū virsrakstus
head_cells = head_line.find_elements(By.TAG_NAME, "td")
# print(len(head_cells))
head_texts = [cell.text.strip() for cell in head_cells]
head_texts[0] = head_texts[0][:11]
# print(head_texts)

car_tr = driver.find_elements(By.CSS_SELECTOR, "tr[id^='tr_']") # dabū visus tr, kuriem id sākas ar tr_
# print(len(car_tr))
# first_car = car_tr[0]
# print(first_car.text)
car_list = []
for i in car_tr:
    # print(i.text)
    data_cells = i.find_elements(By.TAG_NAME, "td")
    car_list.append([cell.text for cell in data_cells if cell.text != ""])

print(car_list)
full_list = []
for car in car_list:
    full_list.append(dict(zip(head_texts, car))) # uztaisa dictionary no visiem datiem

print(full_list)







driver.quit()
