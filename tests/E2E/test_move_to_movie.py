
from logging import log

from playwright.sync_api import Page, expect
from configuration import MAIN_URL


def test_move_to_movie(page: Page):
    page.goto(MAIN_URL)
    page.get_by_role('link', name = 'Фильмы').click()
    expect(page.get_by_test_id('movies_button')).to_be_visible()

def test_go_to_tariffs_with_movie(page: Page):
    page.goto(MAIN_URL)
    page.get_by_role('link', name='Фильмы').click()
    page.get_by_role('link', name='Регистрация и оплата').click()
    expect(page.get_by_text('Регистрация и оплата')).to_be_visible()



