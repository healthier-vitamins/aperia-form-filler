import sys

print(sys.executable)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from dotenv import load_dotenv
import os

load_dotenv()


def main():
    name_env = os.getenv("NAME")
    mobile_env = os.getenv("MOBILE")

    driver = webdriver.Chrome()
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

    # floor_select = Select(
    #     driver.find_element(
    #         By.XPATH, '//*[@id="question-list"]/div[4]/div[2]/div/div/div'
    #     )
    # )
    # floor_select.deselect_all()
    # floor_select.select_by_visible_text("15")

    purpose = driver.find_element(
        By.XPATH,
        '//*[@id="r531850efbc704d2cabb1f836157cd57a_placeholder_content"]/span',
    )
    purpose.clear()
    purpose.send_keys("Meeting")

    # purpose_select = Select(
    #     driver.find_element(
    #         By.XPATH, '//*[@id="question-list"]/div[5]/div[2]/div/div/div'
    #     )
    # )
    # purpose_select.deselect_all()
    # purpose_select.select_by_visible_text("Meeting")


if __name__ == "__main__":
    main()
