from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


PATH = r"D:\Code\drivers\chromedriver-win64(117)\chromedriver-win64\chromedriver.exe"


def accept_google_cookies(wd):
    try:
        # Locate the "Accept all" button by class name
        accept_button = wd.find_element(By.CLASS_NAME, "lssxud")

        # Click the "Accept all" button
        accept_button.click()
        print("Clicked the 'Accept all' button.")
    except Exception as e:
        print("Could not find or click the 'Accept all' button:", str(e))



def search_for_flights(wd):

    try:
        search = 'https://www.google.com/travel/flights'
        wd.get(search)
        accept_google_cookies(wd)

        # Locate, clear & search departure airport
        depart_from = wd.find_element(By.XPATH, "//input[@class='II2One j0Ppje zmMKJ LbIaRd']")
        depart_from.clear()
        depart_from.send_keys('Dublin')
        time.sleep(1)

        #Select the first airport in the dropdown
        select_depart_from = wd.find_element(By.XPATH, "//div[@class='CwL3Ec']")
        select_depart_from.click()
        time.sleep(1)
        
        #Locate & search arrival airport
        fly_to = wd.find_element(By.XPATH, "//input[@placeholder='Where to?']")
        fly_to.send_keys('bangkok')
        time.sleep(1)

        #Select the first airport in the dropdown
        select_fly_to = wd.find_element(By.XPATH, "//div[@class='CwL3Ec']")
        select_fly_to.click()
        time.sleep(1)
        
        #Locate departure date input date
        insert_dep_date = wd.find_element(By.XPATH, "//input[@placeholder='Departure']")
        insert_dep_date.send_keys('2023-10-07')
        insert_dep_date.send_keys(Keys.TAB)
        
        #Locate return date & input date
        insert_ret_date = wd.find_element(By.XPATH, "//input[@placeholder='Return']")
        insert_ret_date.send_keys('2023-10-13')
        insert_ret_date.send_keys(Keys.TAB)
        
        # Locate the search button and click it
        search_button = wd.find_element(By.XPATH, "//button[@jsname='vLv7Lb']")  # Replace "search-button" with the actual class name
        search_button.click()

        # Optional: Wait for a few seconds to allow the search results to load (you can adjust the delay as needed)
        time.sleep(5)

        # Now, you can scrape flight data from the search results page
        # Modify this part to extract the flight data as per your requirements
        flight_data = wd.page_source  # This captures the entire page source, you can parse it with BeautifulSoup

        get_flight_prices(flight_data)

    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_flight_prices(flight_data, wd):  
    try:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(flight_data, 'html.parser')


        # Find all <ul> elements
        ul_elements = soup.find_all('ul')

        for ul in ul_elements:
            # Find all <li> elements with class 'pIav2d' inside each <ul> element
            li_elements = ul.find_all('li', class_='pIav2d')

            for item in li_elements:
                # Print the text content of each <li> element
                print(item.text)


    except Exception as e:
        print("An error occurred:", str(e))
        return None


        





if __name__ == "__main__":
    # Initialize the webdriver 
    wd = webdriver.Chrome(PATH)

    # Set an optional delay
    delay = 5

    # Get image data from the web page
    flight_data = search_for_flights(wd)

    # Close the webdriver
    wd.quit()
