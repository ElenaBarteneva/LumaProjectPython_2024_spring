import allure
from pages import advanced_search


@allure.link('https://trello.com/c/kn91s1De')
@allure.feature("Advanced Search")
@allure.title('Empty input fields')
def test_input_fields_are_empty():
    advanced_search.open()
    advanced_search.click_search_button()
    advanced_search.message_text()

@allure.link('https://trello.com/c/X8H9lLun/')
@allure.feature('Advanced Search')
@allure.title('Entering an incorrect price range')
def test_incorrect_price_range():
    advanced_search.open()
    advanced_search.fill_wrong_price_range()
    advanced_search.click_search_button()
    advanced_search.price_range_error_message()

@allure.link('https://trello.com/c/HCQ997pb/')
@allure.feature('Advanced Search')
@allure.title('Entering prohibited characters in the “Price from” and “Price to” fields')
def test_prohibited_characters_in_price():
    advanced_search.open()
    advanced_search.fill_prohibited_characters_in_price()
    advanced_search.click_search_button()
    advanced_search.invalid_number_price_error_message()

@allure.link('https://trello.com/c/fpWChrDR/')
@allure.feature('Advanced Search')
@allure.title('Products found match the search criteria')
def test_correct_results_of_the_advanced_search():
    advanced_search.open()
    advanced_search.search_by_product_name()
    advanced_search.click_search_button()
    advanced_search.check_search_result()