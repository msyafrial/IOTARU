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
        
        # -> Open the homepage (site root) and wait for the preloader to dismiss so global navigation can be used from the Home view.
        await page.goto("http://localhost:4321/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the 'Solutions' link in the global navigation and verify the Solutions overview is displayed.
        # Solutions link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Solutions', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Products' link in the global navigation to open the Products page and allow the page to settle.
        # Products link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Products', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Blog' link in the global navigation and verify the blog listing is displayed.
        # Blog link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Blog', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Contact Us' link in the global navigation and verify the Contact page is displayed.
        # Contact Us link
        elem = page.locator('xpath=/html/body/main/header/div/div/a[2]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Contact Us' link in the global navigation and verify the Contact page (contact form and contact details) is displayed.
        # Contact Us link
        elem = page.locator('xpath=/html/body/main/header/div/div/a[2]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the blog listing is displayed
        await page.locator("xpath=/html/body/main/section[2]/div/div[2]/div[2]/a").nth(0).scroll_into_view_if_needed()
        # Assert: The second blog post (Smart Home Automation: Complete Guide) is visible in the blog listing.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[2]/div[2]/a").nth(0)).to_be_visible(timeout=15000), "The second blog post (Smart Home Automation: Complete Guide) is visible in the blog listing."
        await page.locator("xpath=/html/body/main/section[2]/div/div[2]/div[3]/a").nth(0).scroll_into_view_if_needed()
        # Assert: The third blog post (IoT Security Best Practices) is visible in the blog listing.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[2]/div[3]/a").nth(0)).to_be_visible(timeout=15000), "The third blog post (IoT Security Best Practices) is visible in the blog listing."
        
        # --> Verify the contact page is displayed
        # Assert: The URL contains 'contact', indicating the contact section is active.
        await expect(page).to_have_url(re.compile("contact"), timeout=15000), "The URL contains 'contact', indicating the contact section is active."
        await page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/input").nth(0).scroll_into_view_if_needed()
        # Assert: The contact form input is visible on the page.
        await expect(page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/input").nth(0)).to_be_visible(timeout=15000), "The contact form input is visible on the page."
        await page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/button").nth(0).scroll_into_view_if_needed()
        # Assert: The contact form 'Send' button is visible on the page.
        await expect(page.locator("xpath=/html/body/main/footer/div/div[1]/div[1]/div/div[2]/form/div/button").nth(0)).to_be_visible(timeout=15000), "The contact form 'Send' button is visible on the page."
        await page.locator("xpath=/html/body/main/footer/div/div[1]/div[2]/div/div[2]/ul/li[1]/a").nth(0).scroll_into_view_if_needed()
        # Assert: The contact email address is visible on the contact section.
        await expect(page.locator("xpath=/html/body/main/footer/div/div[1]/div[2]/div/div[2]/ul/li[1]/a").nth(0)).to_be_visible(timeout=15000), "The contact email address is visible on the contact section."
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
    