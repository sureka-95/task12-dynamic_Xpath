# import selenium webdriver to control the browser
# import By module to locate web element using xpath, id, class ,etc
# import time module to pause the webdriver using sleep()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# define function to explore elements it take 2 inputs webdrive and xpath
def explore_element(web_driver, xpath):
    try: # tries to locate the element using its xpath
        element = web_driver.find_element(By.XPATH, xpath)
        # get the output for each by print statement
        print(" Element Info:")# get the output for each by print statement
        print(f"    Tag: {element.tag_name}")
        print(f"    Text: {element.text.strip()}")

        # fine Parent by xpath
        parent = web_driver.find_element(By.XPATH, f"{xpath}/parent::*")
        print(f"\n Parent: {parent.tag_name}")

        #  find Children by xpath and print it numbers
        children = web_driver.find_elements(By.XPATH, f"{xpath}/*")
        print(f"\n Children: {len(children)}")
        for c in children:
            print(" -", c.tag_name)

        # find Ancestors and print it numbers in length
        ancestors = web_driver.find_elements(By.XPATH, f"{xpath}/ancestor::*")
        print(f"\n Ancestors: {len(ancestors)}")
        for a in ancestors:
            print(" -", a.tag_name)

        # find Siblings both following and preceding
        pre_siblings = web_driver.find_elements(By.XPATH, f"{xpath}/preceding-sibling::*")
        fol_siblings = web_driver.find_elements(By.XPATH, f"{xpath}/following-sibling::*")
        print(f"\n Preceding Siblings: {len(pre_siblings)}")
        print(f"  Following Siblings: {len(fol_siblings)}")
        # Preceding/Following in DOM
        preceding = web_driver.find_elements(By.XPATH, f"{xpath}/preceding::*")
        following = web_driver.find_elements(By.XPATH, f"{xpath}/following::*")
        print(f"\n Preceding in DOM: {len(preceding)}")
        print(f" Following in DOM: {len(following)}")

    # if any error occur
    except Exception as e:
        print("Error:", e)

# main coding for the above assigned web elements
driver = webdriver.Chrome()# get chrome
driver.get("https://www.guvi.in/") # goto guvi website
time.sleep(3)  # wait for the page to load

# Use a stable XPath (e.g., by ID or contains text or partial class name)
explore_element(driver, "//p[@id='liveclasseslink']")
explore_element(driver, "//a[@class='rwl3jt-0 my-2 cursor-pointer ml-2 mr-6 text-base font-normal text-gray-500']")
explore_element(driver, "//p[@id='practiceslink']")
explore_element(driver,"//p[@id='resourceslink']")
explore_element(driver,"//p[@id='solutionslink']")
explore_element(driver,"//a[@id='login-btn']")
explore_element(driver,"//a[contains(@class, 'bg-green-500')]")

# quit driver
driver.quit()
