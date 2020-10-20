from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


PATH = "/home/user/Desktop/Chromedriver/chromedriver.exe" #where chromedriver is saved

driver = webdriver.Chrome(PATH)
driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

driver.get('http://www.youtube.com/results?search_query={}'.format(#Enter search paramter))

  """ Spent hours searching a way to click on a specific video. This is the only way it actually worked was taking the full xpath of the <a> tag in the video title
  """
  
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()
time.sleep(20)




