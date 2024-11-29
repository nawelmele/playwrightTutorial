from playwright.sync_api import Playwright, sync_playwright,expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://console-integ.reach5.co/login?r5_request_token=m6cOE6zd9-BXdE0nyn9CkfVU4zQ_V6Z4OC07igkYky8Zy5hzntuKiMsxzaEv6Uscw3jc-tDHr7oqq8qM9Cjdxj2oe5ZhyxjUxU0xLbN-jeV8y69Nt2Y_7MM0_2-Nudfz16XfETAzvX5coTThURFh4xNgA8H9AnZK-5_6MMH-kNWpmWgJNxL8Hx_irJqt1Y1Q4WNjOcYe8JoN4iphXkMySBUZkMIvCfeIJkb76TLrjDcOwiqSQGobrO1FUQxkmVpl1ns0_FrF9TnIIeJOHXCdVjnkUFRvCbXJcwp1H648IrHZxLthwxFldqkTG64fVLpLwSTCD0qwm10IN4nJDIW1hso0iJKVhqPJQbWVVPuqjE0Cjyic9fggsR5NOgd41twP")
    #page.wait_for_load_state("networkidle")
    page.get_by_test_id("identifier").click()
    page.get_by_test_id("identifier").fill("nawel.mele@reach5.co")
    page.get_by_test_id("password").click()
    page.get_by_test_id("password").press("CapsLock")
    page.get_by_test_id("password").fill("Motdepasse2023*")
    page.get_by_test_id("submit").click()
    expect(page.get_by_text("Accounts")).to_be_visible()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
