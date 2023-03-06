import time
from selenium import webdriver
from selene.support.shared import browser
from selene import be, have
import os

FIRSTNAME = 'Bed'
LASTNAME = 'Tester'
EMAIL = 'bedtester001@gmail.com'
MOBILE = '9119119119'
FILE = '6666.jpg'
ADDRESS = 'New-York,15street,234apt'
STATE = 'Uttar Pradesh'
CITY = 'Agra'


def test_web_form(browser_setings):
    car = os.getcwd() + '\\resources\\6666.jpg'
    browser.open(browser.config.base_url + "/automation-practice-form")
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('#RightSide_Advertisement').execute_script('element.remove()')
    browser.element('#firstName').should(be.blank).type(FIRSTNAME)
    browser.element('#lastName').should(be.blank).type(LASTNAME)
    browser.element('#userEmail').should(be.blank).type(EMAIL)
    browser.element('[for=gender-radio-3]').should(be.clickable).click()
    browser.element('#userNumber').should(be.blank).type(MOBILE)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="2"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1988"]').click()
    browser.element('div[class="react-datepicker__day react-datepicker__day--001"]').click()
    browser.element('#subjectsInput').type('E').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(car)
    browser.element('#currentAddress').should(be.blank).type(ADDRESS)
    browser.element('#state').click()

    browser.element('#react-select-3-option-1').should(have.text(STATE)).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.text(CITY)).click()

    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('tr:nth-child(1) td:nth-child(2)').should(have.text(f'{FIRSTNAME} {LASTNAME}'))
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text(EMAIL))
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text('Other'))
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text(MOBILE))
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('01 March,1988'))
    browser.element('tr:nth-child(6) td:nth-child(2)').should(have.text('English'))
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Sports'))
    browser.element('tr:nth-child(8) td:nth-child(2)').should(have.text(FILE))
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text(ADDRESS))
    browser.element('tr:nth-child(10) td:nth-child(2)').should(have.text(f'{STATE} {CITY}'))
    browser.element('#closeLargeModal').click()


"""
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight-1000)")


"""