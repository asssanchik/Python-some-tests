# test autorized in open source site


from playwright.sync_api import Page
import re


def test_request(page: Page):
    page.route()
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name = 'Войти').click()

