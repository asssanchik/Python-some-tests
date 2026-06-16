# test autorized in open source site


from playwright.sync_api import Page, Route
import re, time



def test_request(page: Page):
    def change_request(route: Route):
        data = route.request.post_data
        if data:
            data = data.replace('User413', 'User412')
        route.continue_(post_data = data)

    page.route(re.compile('profile/authenticate/'), change_request)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User413')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name = 'Войти').click()



def test_response(page: Page):
    def change_response(route: Route):
        response = route.fetch()
        data = response.text
        data = data.replace('User412', 'Assan')
        route.fulfill(response = response, body = data)

    page.route(re.compile('profile/412'), change_response )
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name = 'Войти').click()
   # page.get_by_role('link', name = 'Мой профиль').click()
    time.sleep(5)




