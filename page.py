from locators import MainPageLocators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep



class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver



class MainPage(BasePage):
    """Home page action methods come here. I.e. fill searchbox, select drop down, click on button"""

    def send_keys_to_searchbox(self, inputText):
        """Send keys to the search"""
        element = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        element.send_keys(inputText)

    def get_value_from_searchbox(self):
        return self.driver.find_element(*MainPageLocators.SEARCH_BOX).get_attribute('value')

    def clear_searchbox(self):
        self.driver.find_element(*MainPageLocators.SEARCH_BOX).click()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR , '.autocomplete-clear')))
        element.click()

    def get_autocomplete_error(self):
        try:
            self.driver.find_element(*MainPageLocators.SEARCHBOX_AUTOCOMPLETE_ERROR_MESSAGE)
            return True
        except Exception:
            return False

    def select_range_dropdown(self, inputText):
        select = Select(self.driver.find_element(*MainPageLocators.RANGE_DROPDOWN))
        #select.select_by_index(index)
        select.select_by_visible_text(inputText)

    def get_last_searched_text(self):
        return self.driver.find_element(*MainPageLocators.LAST_SEARCHED_DATA).text

    def select_from_dropdown(self, inputText):
        select = Select(self.driver.find_element(*MainPageLocators.FROM_DROPDOWN))
        select.select_by_visible_text(inputText)

    def select_uptil_dropdown(self, inputText):
        select = Select(self.driver.find_element(*MainPageLocators.UPTIL_DROPDOWN))
        select.select_by_visible_text(inputText)

    def click_on_search(self):
        self.driver.find_element(*MainPageLocators.SEARCH_BUTTON).click()
        sleep(1)

    def set_uptil_specific_amt(self, inputText):
        self.driver.find_element(*MainPageLocators.UPTIL_SPECIFIC_AMT).send_keys(inputText)




class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    def if_element_exists(self, *el):
        try:
            self.driver.find_element(*el)
            return True
        except NoSuchElementException:
            return False
        except Exception:
            return False
        return True

    def are_results_found(self):
        return self.if_element_exists(*MainPageLocators.SEARCH_RESULT)

    def are_search_results_for_minimum_values_found(self):
        return self.if_element_exists(*MainPageLocators.SEARCH_RESULT_FOR_MINIMUM_VALUES)

    def get_no_search_result_found_text(self):
        return self.driver.find_element(*MainPageLocators.NO_SEARCH_RESULT_FOUND).text

    def get_malfunctioning_page_text(self):
        return self.driver.find_element(*MainPageLocators.MALFUNCTIONING_PAGE_TEXT).text



