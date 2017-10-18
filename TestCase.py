import unittest
from selenium import webdriver
import page

class Search(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        """Please Comment the relevant webdriver code for browser, In Chrome sometimes Robot verification is being appeaered while opening new instance. 
    	Firefox is more stable for these test cases"""
        
        """ To Run with: CHROME, remove comments for below 3 lines and comment the line for: self.driver = webdriver.Firefox() """
        #options = webdriver.ChromeOptions()
        #options.add_argument("--start-maximized")
        #self.driver = webdriver.Chrome(chrome_options=options)
        
        """ FIREFOX"""
        self.driver = webdriver.Firefox()
        
        #Implicit wait set for 10 seconds
        self.driver.implicitly_wait(10) # seconds
        # Navigates to the Funda HomePage
        self.driver.get("http://www.funda.nl")
    
    def test_search_valid_data(self):
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox('Amsterdam')
        main_page.select_range_dropdown('+ 5 km')
        main_page.select_from_dropdown('€ 75.000')
        main_page.select_uptil_dropdown('€ 500.000')
        main_page.click_on_search()

        search_result_page = page.SearchResultsPage(self.driver)
        result = search_result_page.are_results_found()
        self.assertTrue(result,"Search results not found!!")
        print("test_search_valid_data is PASSED!")


    def test_search_invalid_data(self):
        searchInput = 'qopasdqqqq'
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox(searchInput)
        main_page.click_on_search()
        isErrorPresent = main_page.get_autocomplete_error()
        self.assertTrue(isErrorPresent,"Error message did appear under Searchbox")
        main_page.click_on_search()
        search_result_page = page.SearchResultsPage(self.driver)
        expectedText = "We kunnen "+searchInput +" niet vinden"
        actualText = search_result_page.get_no_search_result_found_text()
        self.assertEqual(actualText, expectedText, "Actual and Expected results are not equal")
        print("tests_search_invalid_data is PASSED!")

    def test_search_special_character_data(self):
        searchInput = '!@#$@%@213'
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox(searchInput)
        main_page.click_on_search()
        self.assertEqual(main_page.get_value_from_searchbox(), searchInput, "Other page should appear even if searched for special characters")
        print("test_search_specail_character_data is PASSED!")

    def test_search_for_minimum_budget(self):
        searchInput = 'Amsterdam'
        range_data = '+ 0 km'
        minimum_amt_from = '€ 0'
        minimum_amt_until = '€ 50.000'
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox(searchInput)
        main_page.select_range_dropdown(range_data)
        main_page.select_from_dropdown(minimum_amt_from)
        main_page.select_uptil_dropdown(minimum_amt_until)
        main_page.click_on_search()
        search_result_page = page.SearchResultsPage(self.driver)
        result=search_result_page.are_search_results_for_minimum_values_found()
        self.assertTrue(result,"Search result not found!!")
        print("test_search_for_minimum_budget is PASSED!")

    def test_search_for_maximum_budget(self):
        searchInput = 'Amsterdam'
        range_data = '+ 15 km'
        maximum_amt_from = '€ 2.000.000'
        maximum_amt_until = 'Geen maximum'
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox(searchInput)
        main_page.select_range_dropdown(range_data)
        main_page.select_from_dropdown(maximum_amt_from)
        main_page.select_uptil_dropdown(maximum_amt_until)
        main_page.click_on_search()
        search_result_page = page.SearchResultsPage(self.driver)
        result=search_result_page.are_results_found()
        self.assertTrue(result,"Search results not found!!")
        print("test_search_for_maximum_budget is PASSED!")

    def test_verify_X_button_on_searchbox_is_working(self):
        searchInput = 'QWERTYUIOP'
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox(searchInput)
        writtenTextOnSearchBox = main_page.get_value_from_searchbox()
        self.assertEqual(writtenTextOnSearchBox, searchInput,"Actual and Expected results are not equal")
        main_page.clear_searchbox()
        writtenTextOnSearchBox = main_page.get_value_from_searchbox()
        self.assertEqual(writtenTextOnSearchBox, "","Actual and Expected results are not equal")
        print("test_verify_X_button_on_searchbox_is_working is PASSED!")

    def test_verify_the_last_search_result(self):
        searchInput = 'Amsterdam'
        range_data = '+ 10 km'
        amt_from = '€ 50.000'
        amt_until = '€ 300.000'
        main_page = page.MainPage(self.driver)
        main_page.send_keys_to_searchbox(searchInput)
        main_page.select_range_dropdown(range_data)
        main_page.select_from_dropdown(amt_from)
        main_page.select_uptil_dropdown(amt_until)
        main_page.click_on_search()
        search_result_page = page.SearchResultsPage(self.driver)
        result = search_result_page.are_results_found()
        self.assertTrue(result,"Search results not found!!")
        self.driver.get("http://www.funda.nl")
        expectedText = 'Gemeente Amsterdam'+', '+range_data.replace(" ", "")+", "+amt_from+" - "+amt_until
        actualText = main_page.get_last_searched_text()
        self.assertEqual(actualText, expectedText,"Actual and Expected results are not equal")
        print("test_verify_the_last_search_result is PASSED!")

    def test_verify_all_properties_should_visible_when_no_searchText_added(self):
        main_page = page.MainPage(self.driver)
        main_page.click_on_search()
        search_result_page = page.SearchResultsPage(self.driver)
        result=search_result_page.are_results_found()
        self.assertTrue(result,"Search results not found!!")
        print("test_verify_all_properties_should_visible_when_no_searchText_added is PASSED!")
    
    """ Below test case is not so important """
    # def test_verfiy_0_search_result_found(self):
    #     searchInput = 'Gemeente Amsterdam'
    #     range_data = '+ 10 km'
    #     amt_from = '€ 50.000'
    #     amt_until = 'Anders'
    #     specific_amt_uptil = '1'
    #     main_page = page.MainPage(self.driver)
    #     main_page.send_keys_to_searchbox(searchInput)
    #     main_page.select_range_dropdown(range_data)
    #     main_page.select_from_dropdown(amt_from)
    #     main_page.select_uptil_dropdown(amt_until)
    #     main_page.set_uptil_specific_amt(specific_amt_uptil) // Element is not being appeared
    #     main_page.click_on_search()
      
    #     search_result_page = page.SearchResultsPage(self.driver)
    #     result=search_result_page.are_results_found()
    #     self.assertTrue(result,"Search results not found!!")

    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()