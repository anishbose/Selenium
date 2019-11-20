from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os


#link = 'https://www.eventbrite.com/e/austin-area-jazz-festival-2019-tickets-68815754775?aff=ebdssbdestsearch'
link = 'https://www.eventbrite.com/e/x-ica-the-official-jhalak-afterparty-tickets-81235865661'


ticket_x = '/html/body/main/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/form/span/span/button'
frame_x = '/html/body/iframe'
frame_text_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/h2'
num_tix_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div[1]/form/div/div/ul/li[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/select/option[2]'
checkout_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[2]/div/nav/div/button'

# the # of forks you have will generate 2^(# of forks) webpages


driver = webdriver.Chrome()

# Open webpade
driver.get(link)
wait = WebDriverWait(driver, 4)
driver.maximize_window()
action = ActionChains(driver)

# TODO wait for page to load
#time.sleep(2)
while True:
	try:
		ticket = driver.find_element(By.XPATH, ticket_x)
		break
	except:
		driver.refresh()
#ticket = driver.find_element(By.XPATH, ticket_x)
ticket.click()

# TODO wait for frame to load
time.sleep(1)
frame = wait.until(EC.element_to_be_clickable((By.XPATH, frame_x)))
# Switch to num tickets checkout frame
#frame = driver.find_element(By.XPATH, frame_x)
driver.switch_to_frame(frame)

#num_tix = driver.find_element(By.XPATH, num_tix_x)
#num_tix.click()

checkout = driver.find_element(By.XPATH, checkout_x)
checkout.click()


os._exit(0)




