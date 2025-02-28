# if __name__ == "__main__" and __package__ is None:
#     import os
#     import sys

#     # Add the parent directory to the sys.path so the package can be found
#     parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     sys.path.insert(0, parent_dir)
#     __package__ = "selenium_files"

import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium_files.config import FORM_FIELDS
from selenium_files.driver import driver

load_dotenv()


def execute_selenium_script():
    try:
        # Template to search for label name then get the input right after.
        EDITABLE_FIELD_XPATH_TEMPLATE = (
            "//div[@data-automation-id='questionItem'][.//span[contains(., '{0}')]]"
            "//input"
        )

        # Get dropdown field based on label, then return the "Select your answer" field
        DROPDOWN_FIELD_XPATH_TEMPLATE = (
            "//div[@data-automation-id='questionItem'][.//span[contains(., '{0}')]]"
            "//span[contains(., 'Select your answer')]"
        )

        # Get the dropdown list element (to select your choice from dropdown menu)
        # ! For dropdown list there are 2 xpaths since it requires 2 separate actions.
        # ! 1. Click on Select your answer to show dropdown menu
        # ! 2. Click on desired dropdown option
        DROPDOWN_LIST_XPATH_TEMPLATE = (
            "//div[@role='listbox']"
            "//div[@role='option'][.//span[@aria-label='{0}']]"
            "//span[@aria-label='{0}']"
        )

        RADIO_FIELD_XPATH_TEMPLATE = (
            "//div[@data-automation-id='questionItem'][.//span[contains(., '{0}')]]"
            "//div[@role='radiogroup']"
            "//input[@value='{1}']"
        )

        NEXT_BUTTON_XPATH_TEMPLATE = "//button[@aria-label='Next']"

        SUBMIT_BUTTON_XPATH_TEMPLATE = "//button[@data-automation-id='submitButton']"

        SUCCESS_XPATH_TEMPLATE = "//div[@data-automation-id='thankYouMessage']"

        # Get name and number from env
        name_env = os.getenv("NAME")
        mobile_env = os.getenv("MOBILE")

        if not name_env or not mobile_env:
            raise Exception("Env variables missing")

        # *************************************************************
        # *** Fill in name ********************************************
        # *************************************************************
        # Replace with form's label
        name_xpath = EDITABLE_FIELD_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["NAME"] or ""
        )
        name = driver.find_element(By.XPATH, name_xpath)
        name.clear()
        name.send_keys(name_env)

        driver.implicitly_wait(2)

        # *************************************************************
        # *** Select Access level dropdown ****************************
        # *************************************************************
        access_levels_xpath = DROPDOWN_FIELD_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["ACCESS_LEVELS"]["FIELD"] or ""
        )
        access_levels = driver.find_element(By.XPATH, access_levels_xpath)
        access_levels.click()

        selected_level_xpath = DROPDOWN_LIST_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["ACCESS_LEVELS"]["DATA"] or ""
        )
        selected_level = driver.find_element(By.XPATH, selected_level_xpath)
        selected_level.click()

        driver.implicitly_wait(2)

        # *************************************************************
        # *** Select Access level dropdown ****************************
        # *************************************************************
        purpose_xpath = DROPDOWN_FIELD_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["PURPOSE"]["FIELD"] or ""
        )
        purpose = driver.find_element(By.XPATH, purpose_xpath)
        purpose.click()

        selected_level_xpath = DROPDOWN_LIST_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["PURPOSE"]["DATA"] or ""
        )
        selected_level = driver.find_element(By.XPATH, selected_level_xpath)
        selected_level.click()

        driver.implicitly_wait(2)

        # *************************************************************
        # *** Select locally registered number ************************
        # *************************************************************

        purpose_xpath = RADIO_FIELD_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["REGISTERED_NUMBER"]["FIELD"] or ""
        )
        purpose_xpath = purpose_xpath.replace(
            "{1}", FORM_FIELDS["REGISTERED_NUMBER"]["DATA"] or ""
        )

        purpose = driver.find_element(By.XPATH, purpose_xpath)
        purpose.click()

        driver.implicitly_wait(2)

        # *************************************************************
        # *** Click next button ***************************************
        # *************************************************************
        next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH_TEMPLATE)
        next_button.click()

        driver.implicitly_wait(4)

        # *************************************************************
        # *** Click next button ***************************************
        # *************************************************************

        # Replace with form's label
        mobile_xpath = EDITABLE_FIELD_XPATH_TEMPLATE.replace(
            "{0}", FORM_FIELDS["MOBILE"] or ""
        )
        mobile = driver.find_element(By.XPATH, mobile_xpath)
        mobile.clear()
        mobile.send_keys(mobile_env)

        driver.implicitly_wait(3)

        ################################################################

        submit_button = driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH_TEMPLATE)
        submit_button.click()

        # *************************************************************
        # *** Success indicator ***************************************
        # *************************************************************
        # success = driver.find_element(By.XPATH, SUCCESS_XPATH_TEMPLATE)
        # if not success:
        #     raise Exception("Success indicator not found")

    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"{err}")
    finally:
        # driver.quit()
        print("Script completed.")


if __name__ == "__main__":
    execute_selenium_script()
