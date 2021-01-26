import time
import pytest
from selenium.common.exceptions import ElementClickInterceptedException

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
         #"http://selenium1py.pythonanywhere.com/ru/catalogue/hackers-painters_185/"
         ]


@pytest.mark.parametrize('link', links)
def test_check_basket_button_exists(browser, link):
    browser.get(link)
    buttons = len(browser.find_elements_by_xpath('// *[ @ id = "add_to_basket_form"] / button'))
    assert buttons > 0, "NOT FOUND"
    time.sleep(1)
