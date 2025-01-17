from selene import browser
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from selenium.common import StaleElementReferenceException
from pages.locators import BaseLocators as Header
from selenium.webdriver.support.expected_conditions import staleness_of

title_page = s("[data-ui-id='page-title-wrapper']")
list_items = ss("ol.product-items > li.product-item.item.product")
product_images = ss("img.product-image-photo")
grid_mode_option = s(".toolbar.toolbar-products:nth-child(3) > .modes > #mode-grid")
list_mode_option = s(".toolbar.toolbar-products:nth-child(3) > .modes > #mode-list")
selected_view_option = s(".toolbar.toolbar-products:nth-child(3) > .modes > strong[data-value]")
products_wrapper = s("div.products.wrapper")
breadcrumbs = ss(".breadcrumbs li")
product_list = s("ol.product-items")
toolbar_number = s("div.toolbar-products:nth-of-type(2) span.toolbar-number")
position_sort_option = s("option[value='position']")
product_name_sort_option = s("option[value='name']")
price_sort_option = s("option[value='price']")
sorter = s("#sorter")
product_titles = "a.product-item-link"
product_prices = "span>span.price"
men_sale_page_url = 'https://magento.softwaretestingboard.com/promotions/men-sale.html'
breadcrumbs_path = ['Home', 'Sale', 'Men Sale']
page_title = "Men Sale"


def open():
    browser.open(men_sale_page_url)


def get_bread_crumbs():
    breadcrumbs_titles = []
    for i in breadcrumbs:
        breadcrumbs_titles.append(i.locate().text)
    return breadcrumbs_titles


def bread_crumbs_present_should_be_present():
    s(Header.BREADCRUMBS).should(be.present)


def page_title_should_be_present():
    title_page.should(be.present)


def page_title_should_have_correct_text():
    title_page.should(have.text(page_title))


def get_number_of_items_in_te_list():
    return str(len(list_items))


def only_product_cards_for_men_should_be_present():
    for card in product_images:
        card.should(have.attribute("src").value_containing("/m/"))


def product_list_should_be_present():
    product_list.should(be.present)


def number_of_items_in_toolbar_should_correspond_to_amount_in_list():
    toolbar_number.should(have.text(get_number_of_items_in_te_list()))


def selected_view_option_should_be(option: str):
    return selected_view_option.should(have.attribute("data-value").value_containing(option))


def products_in_list_arrangement_should_correspond_to_option(option: str):
    return products_wrapper.should(have.attribute("class").value_containing(option))


def switch_to_display_option(option: str):
    return list_mode_option.click() if option == 'list' else grid_mode_option.click()


def selected_sorting_option_should_be(option: str):
    if option == "Position":
        return position_sort_option.should(have.attribute("selected"))
    elif option == "Product Name":
        return product_name_sort_option.should(have.attribute("selected"))
    elif option == "Price":
        return price_sort_option.should(have.attribute("selected"))


def switch_to_sorting_option(option: str):
    sorter.click()
    if option == "Position":
        position_sort_option.click()
    elif option == "Product Name":
        product_name_sort_option.click()
    elif option == "Price":
        price_sort_option.click()


def product_arrangement_should_correspond_to_sort_option(option: str):
    if option == "Position":
        browser.wait_until(have.url('expected_url'))
        products_arrangement_should_be_sorted_by_position()
    elif option == "Price":
        browser.wait_until(have.url(men_sale_page_url + "?product_list_order=price"))
        products_arrangement_should_be_sorted_by_price()
    elif option == "Product Name":
        browser.wait_until(staleness_of(position_sort_option.locate()))
        products_arrangement_should_be_sorted_by_name()


def products_arrangement_should_be_sorted_by_position():
    position_list = []
    products = ss(product_titles)
    for el in products:
        try:
            position_list.append(el.locate().text.split()[-1])
        except StaleElementReferenceException:
            browser.wait_until(staleness_of(el.locate()))
            position_list.append(el.locate().text.split()[-1])
    sorted_list = sorted(position_list)
    assert position_list == sorted_list, f"Position list is not sorted, actual list: {position_list}"


def products_arrangement_should_be_sorted_by_price():
    prices_list = []
    products = ss(product_prices)
    for el in products:
        try:
            prices_list.append(float(el.locate().text[1:]))
        except StaleElementReferenceException:
            browser.wait_until(staleness_of(el.locate()))
            prices_list.append(float(el.locate().text[1:]))
    sorted_list = sorted(prices_list)
    assert prices_list == sorted_list, f"Price list is not sorted, actual list: {prices_list}"


def products_arrangement_should_be_sorted_by_name():
    names_list = []
    products = ss(product_titles)
    for el in products:
        attempts = 0
        while attempts < 2:
            try:
                name = el.locate().text.strip()
                if name:
                    names_list.append(name)
                    break
            except StaleElementReferenceException:
                attempts += 1
    # Removing empty lines from the list of names before sorting
    names_list = [name for name in names_list if name]
    sorted_list = sorted(names_list)
    assert names_list == sorted_list, f"Name list is not sorted, actual list: {names_list}"
