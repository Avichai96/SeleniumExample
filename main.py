from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = r"./chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.bbc.com/")

# search = driver.find_element(By.CLASS_NAME, "media__link")
# print(search.text)
driver.quit()

# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
try:
    media__link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "media__link"))
    )

    print(type(media__link))
    print(media__link)
finally:
    driver.quit()