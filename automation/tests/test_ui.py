from pathlib import Path
import pytest
playwright = pytest.importorskip("playwright.sync_api")

def test_local_ui():
    with playwright.sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(Path("automation/test_page.html").resolve().as_uri())
        assert page.get_by_role("heading", name="OmniShop").is_visible()
        page.get_by_role("button", name="Add to Cart").click()
        assert page.locator("#cart-count").inner_text() == "1"
        browser.close()
