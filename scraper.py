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
# funda_base_url = "https://www.funda.nl/"

# Send a GET request to the website
response = requests.get(pararius_base_url)

# Check if user is logged in
logged_in = False

if not logged_in:
    # Log in to the website
    login_url = "https://www.pararius.com/login"
    
    login_data = {
        "username": uname,
        "password": pwd
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

# Create a list to store post information
new_posts = []

# Iterate over the first 3 post elements and extract the necessary information
for post in post_elements[:3]:
    type = post.find("h2").text
    address = post.find("div", class_="listing-search-item__sub-title'").text
    new_posts.append({"title": type})
    new_posts.append({"address": address})


# Save the new posts to a new file
new_file_path = "posts/new_posts.json"
with open(new_file_path, "w") as new_file:
    json.dump(new_posts, new_file, indent=2)
    print("New posts saved to:", new_file_path)

# Compare the new file with the old file (if it exists)
old_file_path = "posts/old_posts.json"
if os.path.exists(old_file_path):
    with open(old_file_path, "r") as old_file:
        old_posts = json.load(old_file)

    # Compare the old and new posts
    if old_posts != new_posts:
        print("Changes detected!")

        # Delete the old file
        os.remove(old_file_path)
        print("Old file deleted:", old_file_path)
    else:
        print("No changes detected.")
else:
    print("No old file found.")

# Optionally, save the new posts as the old file for future comparisons
with open(old_file_path, "w") as old_file:
    json.dump(new_posts, old_file, indent=2)
    print("New posts saved as old file:", old_file_path)