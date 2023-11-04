"this is demo"

print("Hello ")

him = "iiiiiiiiiiiiiiiiiiiiiiiii"

for i in  him:
    print(i)
    
    
    
"hii my name is slimshaddy"


from selenium import webdriver
from selenium.webdriver.common.by import By 
from  selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.booking.com/")
driver.maximize_window()


search_box =driver.find_element(By.XPATH,'//*[@id=":re:"]')

key ="GOA"
send_key = search_box.send_keys(key)


pop_up =driver.find_element(By.XPATH,'//*[@id="b2indexPage"]/div[19]/div/div/div/div[1]/div[1]/div/button')
pop_up.click()

sleep(4)
click_button = driver.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[4]/button/span')
click_button.click()
sleep(100)

