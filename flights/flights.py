import flights.costants as const
from datetime import datetime
import logging
import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


class Flights(webdriver.Chrome):
    def __init__(self, driver_path=r"./chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Flights, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()
        self.save_dir = const.SAVE_DIR_FLIGHTS_DATA

        if not os.path.isdir(rf'../{self.save_dir}'):
            os.makedirs(rf'../{self.save_dir}')

    def __exit__(self, exc_type, exc_value, trace):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def get_complited_flights_table(self):
        try:
            num_of_presented_flights = 0
            total_num_of_flight = 10
            while num_of_presented_flights < total_num_of_flight:
                expand_table_butt = self.find_element(By.ID, "next").click()
                num_of_presented_flights = int(self.find_element(By.ID, "numOfResults").text)
                total_num_of_flight = int(self.find_element(By.ID, "totalItems").text)
        finally:
            print(num_of_presented_flights, total_num_of_flight)

    def stop_auto_update_page(self):
        auto_update_toggle = self.find_element(By.ID, "toggleAutoUpdate")
        if str(auto_update_toggle.text) in ['עצור עדכון אוטומטי']:
            auto_update_toggle.click()

    def save_filghts_data_in_json(self):
        filename = self.create_filename()
        flights_data = self.get_flighte_table_data()
        if flights_data:
            with open(rf"../FlightsData/{filename}.json", "w", encoding="utf8") as outfile:
                json.dump(flights_data, outfile, ensure_ascii=False)

    def get_flighte_table_data(self):
        filghts_data_list = []
        table_data = WebDriverWait(self, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[starts-with(@class, 'flight_row')]")))
        for index, item in enumerate(table_data):
            try:
                logging.info(f"flight table item index --> {index}")
                airline =  item.find_element(By.CLASS_NAME, "td-airline").text
                flight =  item.find_element(By.CLASS_NAME, "td-flight").text
                status =  item.find_element(By.CLASS_NAME, "td-status").text
                city = item.find_element(By.CLASS_NAME, "td-city").text
                terminal =  item.find_element(By.CLASS_NAME, "td-terminal").text
                scheduledTime =  str(item.find_element(By.CLASS_NAME, "td-scheduledTime").text).replace('\n', ' ')
                updatedTime =  item.find_element(By.CLASS_NAME, "td-updatedTime").text
                
                filghts_data_list.append(
                    {
                        "airline": airline, 
                        "flight": flight, 
                        "status": status, 
                        "city": city, 
                        "terminal": terminal, 
                        "scheduledTime": scheduledTime, 
                        "updatedTime": updatedTime, 
                    }
                )
            except Exception as e:
                print(repr(e))
                
        return filghts_data_list

    def create_filename(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")
