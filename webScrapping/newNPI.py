from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://npiregistry.cms.hhs.gov/search")

# Wait for the search field to be available
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search-text"))
)

# Enter search term (e.g. a name or NPI number)
search_box.clear()
search_box.send_keys("john doe")

# Click Search button
search_button = driver.find_element(By.ID, "search-button")
search_button.click()

# Wait for results
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "provider-card"))
)

# Extract provider names
cards = driver.find_elements(By.CLASS_NAME, "provider-card")
results = ""
for card in cards:
    try:
        name = card.find_element(By.CLASS_NAME, "provider-name").text
        print(name)
        results += name + "\n"
    except:
        continue

# Save to file
with open("newNpi.txt", "w", encoding="utf-8") as f:
    f.write(results)

input("Press Enter to close browser...")
driver.quit()
