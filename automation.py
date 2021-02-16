from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("please scan qr code and press any key")

RM = driver.find_element_by_css_selector('span[title="Printing 3rd Years"]')

RM.click()

testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
for i in range(150):
    testinput.send_keys("Hii Welcome to whatsapp")
    testinput.send_keys("ganja kwaba bhailog")
    testinput.send_keys(Keys.RETURN)


