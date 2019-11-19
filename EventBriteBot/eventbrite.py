from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


link = 'https://www.eventbrite.com/e/austin-area-jazz-festival-2019-tickets-68815754775?aff=ebdssbdestsearch'

ticket_x = '/html/body/main/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/form/span/span/button'
frame_x = '/html/body/iframe'
frame_text_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/h2'
num_tix_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div[1]/form/div/div/ul/li[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/select/option[2]'
checkout_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[2]/div/nav/div/button'

first_name_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[1]/div/div[1]/div/div[1]/div/div/input'
last_name_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[1]/div/div[2]/div/div[1]/div/div/input'
email_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[1]/div/div[3]/div/div[1]/div/div/input'
card_selection_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/div/ul/li[1]/div[1]/button/div'
card_number_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/div[3]/div/div/div/main/div[1]/div/div[1]/div/div/input'
card_exp_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/div[3]/div/div/div/main/div[2]/div/div[1]/div/div/input'
card_sec_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/div[3]/div/div/div/main/div[3]/div/div[1]/div/div/input'
card_zip_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/div[2]/div[2]/div[3]/div/div/div/main/div[4]/div/div[1]/div/div/input'
no_emails_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/section/section[2]/div/label[1]/span/div[2]/i/svg'
submit_x = '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[2]/div/nav/div/button'

form_first_name = 'Anish'
form_last_name = 'Bose'
form_email = 'anishbose26@gmail.com'
form_card_number = '4505555674182113'
# type using 4 consecutive #s, MMYY (no slash) -> 03/2020 becomes 0320
form_card_exp = '1121'
form_card_sec = '916'
form_card_zip = '78613'


driver = webdriver.Chrome()

# Open webpade
driver.get(link)
wait = WebDriverWait(driver, 4)
driver.maximize_window()
action = ActionChains(driver)

# TODO wait for page to load
#time.sleep(2)
ticket = wait.until(EC.element_to_be_clickable((By.XPATH, ticket_x)))
#ticket = driver.find_element(By.XPATH, ticket_x)
ticket.click()

# TODO wait for frame to load
time.sleep(1)
frame = wait.until(EC.element_to_be_clickable((By.XPATH, frame_x)))
# Switch to num tickets checkout frame
#frame = driver.find_element(By.XPATH, frame_x)
driver.switch_to_frame(frame)

num_tix = driver.find_element(By.XPATH, num_tix_x)
num_tix.click()

checkout = driver.find_element(By.XPATH, checkout_x)
checkout.click()

driver.switch_to.default_content()

# TODO wait for frame to load
time.sleep(3)
frame = wait.until(EC.element_to_be_clickable((By.XPATH, frame_x)))
#frame = driver.find_element(By.XPATH, frame_x)
driver.switch_to_frame(frame)

# Fill out form
name = driver.find_element(By.XPATH, first_name_x)
name.send_keys(form_first_name)

last_name = driver.find_element(By.XPATH, last_name_x)
last_name.send_keys(form_last_name)

email = driver.find_element(By.XPATH, email_x)
email.send_keys(form_email)

card_selection = driver.find_element(By.XPATH, card_selection_x)
card_selection.click()

card_number = driver.find_element(By.XPATH, card_number_x)
card_number.send_keys(form_card_number)

card_exp = driver.find_element(By.XPATH, card_exp_x)
card_exp.send_keys(form_card_exp)

card_sec = driver.find_element(By.XPATH, card_sec_x)
card_sec.send_keys(form_card_sec)

card_zip = driver.find_element(By.XPATH, card_zip_x)
card_zip.send_keys(form_card_zip)


frame_text = driver.find_element(By.XPATH, frame_text_x)
frame_text.click()

action_start_key_down = ActionChains(driver).key_down(Keys.DOWN)
action_end_key_down = ActionChains(driver).key_up(Keys.DOWN)

#TODO until checkbox element visible
for i in range(20):
	action_start_key_down.perform()
action_end_key_down.perform()

no_emails = driver.find_element(By.XPATH, '/html/body/div/div/div/dialog/div[1]/div[1]/div/main/div/div[1]/div/div/form/section/section[2]/div/label[2]/span')
no_emails.click()
no_emails.click()

#submit = driver.find_element(By.XPATH, submit_x)
#submit.click()


print('done')




