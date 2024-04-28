import sys

# check for python on local environment
print(sys.executable)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os

load_dotenv()


def main():
    try:
        name_env = os.getenv("NAME")
        mobile_env = os.getenv("MOBILE")

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        driver.get(
            "https://forms.office.com/pages/responsepage.aspx?id=WGeXB8aT70uz3FOGA9yRbsbr_tTOC29AvupnhyEvx8FUQzNRMkFROE5ZVTRQSU8yQVZEQlg4SDBCSCQlQCN0PWcu"
        )

        name = driver.find_element(
            By.XPATH, '//*[@id="question-list"]/div[1]/div[2]/div/span/input'
        )
        name.clear()
        name.send_keys(name_env or "")

        mobile = driver.find_element(
            By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/span/input'
        )
        mobile.clear()
        mobile.send_keys(mobile_env or "")

        floor = driver.find_element(
            By.XPATH, '//*[@id="question-list"]/div[4]/div[2]/div/div/div'
        )
        floor.click()

        floor_dropdown_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[14]"))
        )

        if floor_dropdown_element:
            floor_fifteen_dropdown = driver.find_element(
                By.XPATH, "/html/body/div[2]/div/div[14]"
            )
            floor_fifteen_dropdown.click()

        purpose = driver.find_element(
            By.XPATH,
            '//*[@id="question-list"]/div[5]/div[2]/div/div/div',
        )
        purpose.click()

        purpose_dropdown_element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                # (By.CLASS_NAME, "this-definitely-does-not-exist")
                (By.XPATH, "/html/body/div[2]/div/div[3]")
            )
        )

        if purpose_dropdown_element:
            purpose_meeting_dropdown = driver.find_element(
                By.XPATH, "/html/body/div[2]/div/div[3]"
            )
            purpose_meeting_dropdown.click()

        submit = driver.find_element(
            By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button'
        )
        submit.click()

        driver.implicitly_wait(5)

        find_by_xpath = driver.find_element(
            By.XPATH,
            '//*[@id="form-main-content1"]/div/div/div[2]/div[1]/div[2]/div[2]/span/text()',
        )
        find_by_text = driver.find_element(
            By.XPATH, "//a[contains(text(), 'You have registered successfully')]"
        )

        print("find_by_xpath: ", find_by_xpath)
        print("find_by_text: ", find_by_text)

    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    finally:
        # driver.quit()
        print("script finished running")


if __name__ == "__main__":
    main()
