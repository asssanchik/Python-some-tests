
from logging import log

from playwright.sync_api import Page, expect
from configuration import MAIN_URL


def test_move_to_movie(page: Page):
    page.goto(MAIN_URL)
    page.get_by_role('link', name = 'Фильмы').click()
    expect(page.get_by_test_id('movies_button')).to_be_visible()
