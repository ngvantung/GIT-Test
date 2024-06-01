#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = r'C:\Users\tnguy110\Desktop\Py work\automation-main\2.Automate The News\chromedriver.exe'

# Create the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

# Wait for the elements to fully load
wait = WebDriverWait(driver, 10)
containers = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]')))

titles = []
subtitles = []
for container in containers:
    title = "Title not found"
    subtitle = "Subtitle not found"

    try:
        title_element = container.find_element(By.XPATH, './/span[contains(@class, "teaser__headline")]')
        title = title_element.text
    except Exception as e:
        print(f"Title not found in this container: {container.get_attribute('innerHTML')}")

    try:
        subtitle_element = container.find_element(By.XPATH, './/h3[contains(@class, "teaser__subdeck")]')
        subtitle = subtitle_element.text
    except Exception as e:
        print(f"Subtitle not found in this container: {container.get_attribute('innerHTML')}")

    titles.append(title)
    subtitles.append(subtitle)

# Exporting data to a CSV file
df_headlines = pd.DataFrame({
    'title': titles,
    'subtitle': subtitles
})
csv_path = r'C:\Users\tnguy110\Desktop\headlines.csv'  # Path where the CSV will be saved
df_headlines.to_csv(csv_path, index=False)

driver.quit()

