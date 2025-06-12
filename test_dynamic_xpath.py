# import selenium webdriver to control the browser
# import By module to locate web element using xpath, id, class ,etc
# import time module to pause the webdriver using sleep()
# import  pytest framework using to run and structure the tests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


# define function explore_element and  pass the object webdrive and xpath
def explore_element(web_driver, xpath):

   # try  block used to find main element using the given xpath
   # assign the dynamic xpath for each element like parent,child,sibling,ancestor etc
    try:
        element = web_driver.find_element(By.XPATH, xpath)
        parent = web_driver.find_element(By.XPATH, f"{xpath}/parent::*")
        children = web_driver.find_elements(By.XPATH, f"{xpath}/*")
        ancestors = web_driver.find_elements(By.XPATH, f"{xpath}/ancestor::*")
        pre_siblings = web_driver.find_elements(By.XPATH, f"{xpath}/preceding-sibling::*")
        fol_siblings = web_driver.find_elements(By.XPATH, f"{xpath}/following-sibling::*")
        preceding = web_driver.find_elements(By.XPATH, f"{xpath}/preceding::*")
        following = web_driver.find_elements(By.XPATH, f"{xpath}/following::*")

        # return all the data collected from Try  and  form a dictionary
        return {
            "tag": element.tag_name,
            "text": element.text.strip(),
            "parent_tag": parent.tag_name,
            "children_count": len(children),
            "ancestors_count": len(ancestors),
            "preceding_siblings": len(pre_siblings),
            "following_siblings": len(fol_siblings),
            "preceding": len(preceding),
            "following": len(following)
        }
    # use exception if there's an error or element not found the error message displayed
    except Exception as e:
        return {"error": str(e)}

# fixtures for setup the browser and tear down
# scope="module" for reuse this fixture for all test in a file
# get the website and yield and quit after the tests complete
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    time.sleep(3)
    yield driver
    driver.quit()
# positive test cases for valid the links for those given below
@pytest.mark.parametrize("xpath", [
    "//p[@id='liveclasseslink']",
    "//p[@id='practiceslink']",
    "//p[@id='resourceslink']",
    "//p[@id='solutionslink']",
    "//a[@id='login-btn']"
])

#  define method to asser there is no error ,tag name not empty
#  child and ancestor count


def test_explore_valid(driver, xpath):
    result = explore_element(driver, xpath)
    assert "error" not in result, f"Error found in {xpath}"
    assert result["tag"] != ""
    assert isinstance(result["children_count"], int)
    assert isinstance(result["ancestors_count"], int)

# fixtures for negative test cases which check invalid paths
@pytest.mark.parametrize("xpath", [
    "//p[@id='wrongid']",
    "//a[@class='not-present-class']"
])

# negative test cases assert the results
def test_explore_invalid(driver, xpath):
    result = explore_element(driver, xpath)
    assert "error" in result
    assert "no such element" in result["error"].lower()
