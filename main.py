
from articales.articales import Articles
from flights.flights import Flights
from searcher.searcher import Searcher
import os

BBC_ARTICALE_DIR = r"../BBCArticales"
FLIGHTS_DATA_DIR = r"../FlightsData"
CONTENT_TO_SEARCH = "PC 777"
# CONTENT_TO_SEARCH = "Stay with"

with Searcher(content_to_search=CONTENT_TO_SEARCH, target_dir=FLIGHTS_DATA_DIR) as srch:
	try:
		print(srch.search_in_txt())
	except Exception as e:
		print(repr(e))

	try:
		print(srch.search_in_json())
	except Exception as e:
		print(repr(e), "\n You are trying to run the function \"search_in_json\" not on json file ")


try:
    with Articles() as art:
        art.land_first_page()
        art.get_all_articales_link()
        art.extract_articles_and_save()
        print("Exiting...")


    with Flights() as fli:
        fli.land_first_page()
        fli.get_complited_flights_table()
        fli.stop_auto_update_page()
        fli.save_filghts_data_in_json()
        print("Exiting...")

except Exception as e:
    if 'in PATH' in str(e):
        print(
            "You are trying to run from command line \n"
            "Pliease add to PATH your selenium Drivers \n"
            "Windows: \n"
            "         set PATH=%PATH%;C:<path-to-your-directory \n \n"
            "Linux: \n"
                      "PATH=$PATH:/path/toyour/folder/ \n"
            "Mac: \n"
                      "xattr -d com.apple.quarantine chromedriver \n"
        )
    else:
        raise
