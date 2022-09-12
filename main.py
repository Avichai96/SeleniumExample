
from articales.articales import Articles
from flights.flights import Flights

# with Articles() as art:
#     art.land_first_page()
#     art.get_all_articales()
#     print("Exiting...")


with Flights() as fli:
    fli.land_first_page()
    fli.get_complited_flights_table()
    fli.stop_auto_update_page()
    fli.save_filghts_data_in_json()
    print("Exiting...")


# save_articles = Articles()
# save_articles.get_all_articales()


# search = driver.find_elements(By.CLASS_NAME, "media__link")
# print([i.text for i in search])
# driver.quit()
