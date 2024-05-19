from selene import have
from selene.support.conditions import be
from selene.support.shared.jquery_style import ss

from data.links import SALE_PAGE_URL, WOMEN_JACKET_LINK
from pages.base_page import BasePage
from pages.locators import SalePageLocators, BaseLocators
from selene import browser, have
from selene.support.shared.jquery_style import s, ss


def visit():
    browser.open(SalePageLocators.LINK_WOMEN_SALE)


def check_if_breadcrumbs_have_all_parts():
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale'))


def visit_women_jackets():
    browser.open(WOMEN_JACKET_LINK)


def visit_sale():
    browser.open(SALE_PAGE_URL)


def is_mens_deals_img_visible():
    s(SalePageLocators.MENS_DEALS_IMG).should(be.visible)


def is_mens_deals_img_clickable():
    s(SalePageLocators.MENS_DEALS_IMG).should(be.clickable)

def click_mens_deals_img():
    s(SalePageLocators.MENS_DEALS_IMG).click()
    
def check_redirection_mens_deals():
    assert browser.driver.current_url == 'https://magento.softwaretestingboard.com/promotions/men-sale.html'


def is_stretch_your_budget_text_visible():
    s(SalePageLocators.STRETCH_YOUR_BUDGET_TEXT).should(have.text('Stretch your budget with active attire'))


def is_mens_bargains_text_visible():
    s(SalePageLocators.MENS_BARGAINS_TEXT).should(have.text('Men’s Bargains'))


def is_shop_mens_deals_text_visible():
    s(SalePageLocators.SHOP_MENS_DEALS).should(have.text('Shop Men’s Deals'))


class SalePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_page(self):
        self.visit(SALE_PAGE_URL)

    def check_page_title(self):
        self.assert_text_of_element("h1.page-title", 'Sale')

    def redirect(self):
        self.browser.should(have.url(SALE_PAGE_URL))
