import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("to be deleted")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("223")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_test_id("todo-title").hover()
