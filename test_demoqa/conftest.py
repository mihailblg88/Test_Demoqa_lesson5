import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_setings():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 6.0
