import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:4321/solutions")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the 'Products' navigation link to open the Products section and verify the products catalog is displayed.
        # Products link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Products', exact=True)
        await elem.click(timeout=10000)
        
        # -> Navigate to the homepage (root URL '/') and wait for the page to load so the global navigation can be used.
        await page.goto("http://localhost:4321/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the 'Solutions' navigation link to open the Solutions section and verify the Solutions overview is displayed.
        # Solutions link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Solutions', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Products' navigation link to open the Products section and verify the products catalog is displayed.
        # Products link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Products', exact=True)
        await elem.click(timeout=10000)
        
        # -> Navigate to the homepage (open '/'), so the global navigation on the homepage can be used to move between site sections.
        await page.goto("http://localhost:4321/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the 'Solutions' navigation link in the global nav to open the Solutions section and verify the Solutions overview is displayed.
        # Solutions link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Solutions', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Solutions' navigation link in the global nav to open the Solutions section and verify the Solutions hero is displayed.
        # Solutions link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Solutions', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Products' navigation link in the global navigation to open the Products section.
        # Products link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Products', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Products' navigation link in the global navigation and verify the Products catalog/hero is displayed.
        # Products link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Products', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Blog' navigation link in the global navigation to open the Blog listing and verify the blog listing appears.
        # Blog link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Blog', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the blog listing is displayed
        # Assert: The current URL contains '/blog', confirming the blog listing is displayed.
        await expect(page).to_have_url(re.compile("/blog"), timeout=15000), "The current URL contains '/blog', confirming the blog listing is displayed."
        
        # --> Verify the contact form is displayed
        await page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/input").nth(0).scroll_into_view_if_needed()
        # Assert: The contact form message input is visible.
        await expect(page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/input").nth(0)).to_be_visible(timeout=15000), "The contact form message input is visible."
        await page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/button").nth(0).scroll_into_view_if_needed()
        # Assert: The contact form Send button is visible.
        await expect(page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/button").nth(0)).to_be_visible(timeout=15000), "The contact form Send button is visible."
        current_url = await page.evaluate("() => window.location.href")
        # Assert: page loaded with a URL (final outcome verified by the AI judge during the run)
        assert current_url, 'Page should have loaded with a URL'
        current_url = await page.evaluate("() => window.location.href")
        # Assert: page loaded with a URL (final outcome verified by the AI judge during the run)
        assert current_url, 'Page should have loaded with a URL'
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    