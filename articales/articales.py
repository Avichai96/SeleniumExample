import os
import logging
import articales.constants as const
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


class Articles(webdriver.Chrome):

    def __init__(self, driver_path=r"./chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Articles, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.save_dir = const.SAVE_DIR_BBC_ARTOCALES
        self.article_link_list = []

        if not os.path.isdir(rf'../{self.save_dir}'):
            os.makedirs(rf'../{self.save_dir}')

    def __exit__(self, exc_type, exc_value, trace):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def get_all_articales_link(self):
        try:
            articles_link_list = WebDriverWait(self, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[starts-with(@class, 'media__link')]"))
            )
        except:
            raise

        for item in articles_link_list:
            self.article_link_list.append(str(item.get_attribute('href')))

    def extract_articles_and_save(self):
        if self.article_link_list:
            total_article_num = len(self.article_link_list)
            for index, link in enumerate(self.article_link_list):
                self.get(link)
                try:
                    article_title = self.find_element(By.ID, 'main-heading').get_attribute('innerHTML').strip()
                except:
                    article_title = "<no title>"

                if link.startswith(const.BASE_URL):
                    filename = str(link).split(const.BASE_URL)[1].replace('/', '_')
                else:
                    filename = str(link).split('/')[-1]

                if not os.path.isfile(rf"../{self.save_dir}/{filename}.txt"):
                    text = WebDriverWait(self, 20).until(
                        EC.presence_of_all_elements_located((By.TAG_NAME, 'p'))
                    )
                    content = " ".join([i.text for i in text])
                    logging.info(f"--> saving --> {index+1}/{total_article_num}")
                    with open(rf"../{self.save_dir}/{filename}.txt", "w") as outfile:
                        outfile.write(f"link: {link}\n title: {article_title}\n{content}")
                else:
                    continue

