import os
import articales.constants as const
from selenium import webdriver

from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC


class Articles(webdriver.Chrome):

    def __init__(self, driver_path=r"./chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Articles, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.save_dir = const.SAVE_DIR_BBC_ARTOCALES

        if not os.path.isdir(rf'../{self.save_dir}'):
            os.makedirs(rf'../{self.save_dir}')

    def __exit__(self, exc_type, exc_value, trace):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def get_all_articales(self):
        articles_list = self.find_elements(By.CLASS_NAME, "media__link")
        print(articles_list)
        articles_list.clear()
        print("-->", articles_list)

# class Articles(object):
    # def __init__(self):
    #     PATH = r"./chromedriver"
    #     self.driver = webdriver.Chrome(PATH)
    #     self.action = ActionChains(self.driver)
    #     self.driver.get("https://www.bbc.com/")
    #     self.save_dir = "BBCArticales"
    #     self.articles_list = []
    #     # self.driver.implicitly_wait(30)

    #     if not os.path.isdir(rf'../{self.save_dir}'):
    #         os.makedirs(rf'../{self.save_dir}')

    # def __exit__(self, exc_type, exc_value, trace):
    #     pass

    # def get_all_articales(self):
    #     try:
    #         self.articles_list = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_all_elements_located((By.CLASS_NAME, "media__link"))
    #         )
    #     except:
    #         pass

    #     else:
    #         self.menage_articles_dir()

    #     finally:
    #         self.driver.quit()

    # def menage_articles_dir(self):
    #     for articale_obj in self.articles_list:
    #         link = articale_obj.get_attribute('href')
    #         print("-->", link)
    #         if not os.path.isfile(link.split('/')[-1]):
    #             self.extract_text_from_article(link)
    #             # with open(os.path.join(f"../{self.save_dir}", f"{link}.txt"), 'w') as fp:
    #             #     pass
        
    # def extract_text_from_article(self, link):
    #     pass
        


