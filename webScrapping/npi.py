# import requests
# import json
# import time
# import csv
# import os

# base_url = "https://npiregistry.cms.hhs.gov/api/"

# details = {
#     "version": "2.1",
#     "limit": 50,
#     "skip": 0,
#     "city": "india"
# }

# all_results = []
# tofindtime = 5
# starttime = 0

# while starttime< tofindtime:
#     print(f" (Call = {call_count + 1})")

#     response = requests.get(base_url, details=details)

#     data = response.json()
#     results = data.get("results", [])

#     if not results:
#         print("No more results.")
#         break

#     all_results.extend(results)

#     details["skip"] += 200
#     call_count += 1
#     time.sleep(0.5)


import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# Optional: Use free proxy list
proxies = [
    '103.253.27.202:8080',
    '103.170.120.172:8080',
    '103.48.68.37:83'
]


# Fake user-agent
ua = UserAgent()

def create_driver():
    # proxy = random.choice(proxies)  ❌ Remove this
    user_agent = ua.random

    options = Options()
    # options.add_argument(f'--proxy-server=http://{proxy}') ❌ Comment this
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless=new")  # Optional: run browser in background

    driver = webdriver.Chrome(options=options)
    return driver


def scrape_npi_data():
    driver = create_driver()
    driver.get("https://npiregistry.cms.hhs.gov/search")

    # Wait for page to load JS content
    time.sleep(3)

    # Example: Search for all providers with "John" as first name
    first_name_input = driver.find_element(By.ID, "firstName")
    first_name_input.send_keys("John")

    # Click search
    search_button = driver.find_element(By.XPATH, "//button[contains(text(),'Search')]")
    search_button.click()
    time.sleep(5)

    all_data = []

    while True:
        time.sleep(2)
        results = driver.find_elements(By.CLASS_NAME, "result-container")

        for result in results:
            try:
                name = result.find_element(By.CLASS_NAME, "npi-header").text
                info = result.find_element(By.CLASS_NAME, "npi-details").text
                all_data.append({"Name": name, "Details": info})
            except:
                continue

        # Try going to the next page
        try:
            next_button = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
            if next_button.is_enabled():
                next_button.click()
            else:
                break
        except:
            break

    driver.quit()
    return all_data

# Get data
data = scrape_npi_data()

# Save to Excel
df = pd.DataFrame(data)
df.to_excel("npi_data.xlsx", index=False)
print("✅ Data saved to 'npi_data.xlsx'")
