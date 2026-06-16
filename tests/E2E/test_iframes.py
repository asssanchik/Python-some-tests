from playwright.sync_api import Page
import time


def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    page.frame_locator('iframe').locator('.navbar-toggler-icon').click()



def test_select(page: Page):
    page.goto('https://unicoplay.com/ru/series')
    page.get_by_test_id('sort_dropdown_default').click()
    page.get_by_test_id('sort_dropdown_default').locator('span').filter(has_text='По новизне').click()
    time.sleep(5)
