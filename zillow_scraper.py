"""

Zillow Data Scraper
Author: John Picken

"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


def get_listings(location, path, sleep_time):


# Initialize web driver
    options = webdriver.ChromeOptions()
    
# Open Page

# Remove Boundary

# Pages Loop Starts Here

# Listing Loop Starts Here

# Listing Loop Ends Here

# Next Page

# Pages Loop Ends Here

# Move Listings into dictionary

# return into dataframe

    return pd.DataFrame(listings)