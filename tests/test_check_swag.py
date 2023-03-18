from pages.swag_labs import SwagLabs


def test_exist_icon(browser):
    swag_qa_page = SwagLabs(browser)
    swag_qa_page.visit()
    assert swag_qa_page.exit_icon()


def test_check_name(browser):
    swag_qa_page = SwagLabs(browser)
    swag_qa_page.visit()
    assert swag_qa_page.exit_name()


def test_check_password(browser):
    swag_qa_page = SwagLabs(browser)
    swag_qa_page.visit()
    assert swag_qa_page.exit_password()
