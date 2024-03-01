import requests
from bs4 import BeautifulSoup
import json
import datetime
import os

# Load credentials from environment variables
uname = os.environ.get('SCRAPER_UNAME')
pwd = os.environ.get('SCRAPER_PWD')


# Print the current date and time
current_date_time = datetime.datetime.now()
print("File last ran on:", current_date_time)  

# URL of the website you want to scrape
pararius_base_url = "https://www.pararius.com/apartments/leiden/700-1500"
funda_base_url = "https://www.funda.nl/"

# Send a GET request to the website
response = requests.get(pararius_base_url)

# Check if user is logged in
logged_in = False

if not logged_in:
    # Log in to the website
    login_url = "https://www.pararius.com/login"
    
    login_data = {
        "username": pararius_uname,
        "password": pararius_pwd
    }
    

    login_response = requests.post(login_url, data=login_data)
    
    # Check if login was successful
    if login_response.status_code == 200:
        print("Login successful!")
        logged_in = True
    else:
        print("Login failed!")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
 
# Find the elements containing the posts
post_elements = soup.find_all("li", class_="search-list__item search-list__item--listing")

# Iterate over the post elements and extract the necessary information
for post in post_elements:
    title = post.find("h2").text
    print("Title:", title)