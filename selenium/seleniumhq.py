from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.amazon.co.uk')
#assert 'Amazon' in browser.title

elem = browser.find_element(By.ID, 'twotabsearchtextbox')  # Find the search box
elem.send_keys('Python' + Keys.RETURN)
#browser.quit()