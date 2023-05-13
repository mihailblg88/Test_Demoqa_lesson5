from selene import command
from selene.support.shared import browser
from models.registration_page import RegistrationPage

browser.config.click_by_js = True


def test_registration_page():
    registration_page = RegistrationPage()
    # OPEN PAGE
    registration_page.open()

    # WHEN
    registration_page.type_first_name('Bed')
    registration_page.type_last_name('Tester')
    registration_page.type_email('bedtester001@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.type_number('9119119119')
    registration_page.type_date_of_birth('January', '1988', '11')
    registration_page.type_subjects('English')
    registration_page.choose_hobbies('Sports')
    registration_page.picture_path('/resources/6666.jpg')
    registration_page.type_address('New-York,15street,234apt')
    registration_page.choose_state_and_city('Haryana', 'Karnal')
    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.should_registered_user_with(
        'Bed Tester',
        'bedtester001@gmail.com',
        'Male',
        '9119119119',
        '1 January,1988',
        'English',
        'Sports',
        '6666.jpg',
        'New-York,15street,234apt',
        'Haryana Karnal'
    )
    browser.element('#closeLargeModal').click()



