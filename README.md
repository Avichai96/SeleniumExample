# SeleniumExample

- Fix mac Catalina chromedriver installition: open Terminal > nav to chromedriver.exec > 
Tap: "xattr -d com.apple.quarantine chromedriver"

# Setup
- use pip3/pip install -r requirements or user the venv
- make sure ther is correct chromedriver on yuor device
- choose the model you want to run uncomment it from main.py and use 

# Run 
from main.py 
for Articales Model uncomment the context manager to Articles()
for Flights Model uncomment the context manager to Flights()
for Searcher Model uncomment the context manager to Searcher() and also the right function depanding on the case.


# Articales Model
- create instace to get and save all articals in "bbc.com "
- main methods (in the order):
    land_first_page() -> to get the home page.
    get_all_articales_link() - to get the url's for all articals.
    extract_articles_and_save() - get articale one by one, check if it exists, if not save it as .txt.
- geneally: the articale saved in file where the url is saved in the first line.

# Flights Model
- create instace to get and save all flights table in ".../airports/BenGurion/Pages/OnlineFlights..."
- main methods (in the order):
    land_first_page() -> to get the main page
    get_complited_flights_table() -> expand the table to max size 
    stop_auto_update_page() -> stop the dinamic update that Selenium load all the adta correctly.
    save_filghts_data_in_json() -> creat list of all flight obj and save in json file

# Searcher Model
- get 2 params, content_to_search -> string of content to search
                target_dir -> path to directory (include the name)
- main method:
    search_in_txt() -> serching string in target_dir and return list of results
    search_in_json() -> serching string in target_dir only in json file and return list of results