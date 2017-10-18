from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_BOX = (By.ID, 'autocomplete-input')
    SEARCHBOX_CLEAR_BUTTON = (By.CSS_SELECTOR , '.autocomplete-clear')
    SEARCHBOX_AUTOCOMPLETE_ERROR_MESSAGE = (By.CSS_SELECTOR , '.autocomplete-no-suggestion-message')
    LAST_SEARCHED_DATA = (By.CSS_SELECTOR , '.link-alternative')
    UPTIL_SPECIFIC_AMT = (By.CSS_SELECTOR , ':not(.is-inactive) .input-number-field')
    RANGE_DROPDOWN = (By.ID, 'Straal')
    FROM_DROPDOWN = (By.ID, 'range-filter-selector-select-filter_koopprijsvan')
    UPTIL_DROPDOWN = (By.ID, 'range-filter-selector-select-filter_koopprijstot')
    SEARCH_BUTTON = (By.CSS_SELECTOR , '.button-primary-alternative')
    SEARCH_RESULT = (By.CSS_SELECTOR , '.search-content-output .top-position')
    NO_SEARCH_RESULT_FOUND = (By.CSS_SELECTOR , '.location-suggestions-header-content')
    MALFUNCTIONING_PAGE_TEXT = (By.CSS_SELECTOR , '.app-error-hero-title')
    SEARCH_RESULT_FOR_MINIMUM_VALUES = (By.CSS_SELECTOR , '.search-output-result-count+.search-results')

