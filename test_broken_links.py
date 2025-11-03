import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

def test_broken_links():

   
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Website to test
    url = "https://practicetestautomation.com/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

   
    links = driver.find_elements(By.TAG_NAME, "a")

    results = []

    for link in links:
        href = link.get_attribute("href")

       
        if href is None or "javascript" in href.lower():
            continue

        try:
            response = requests.get(href, timeout=5)
            status = response.status_code

            if status >= 400:
                results.append([href, "BROKEN", status])
            else:
                results.append([href, "WORKING", status])

        except Exception:
            results.append([href, "BROKEN", "Timeout/Error"])

    driver.quit()

    
    df = pd.DataFrame(results, columns=["URL", "Status", "Code"])
    df.to_csv("reports/broken_links_report.csv", index=False)

   
    broken_count = df[df["Status"] == "BROKEN"].shape[0]
    print(f"Total Broken Links: {broken_count}")

   
    assert True


